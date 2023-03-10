from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django_ratelimit.decorators import ratelimit
from PIL import Image

from .utils import *
from .forms import LoginForm, UploadImageForm


def home(request):
    return render(request, 'dapp/home.html')


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)


@ratelimit(key='ip', rate='3/m', method=['POST'], block=True)
@login_required
def upload_image(request):
    form = UploadImageForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():

        fields = None
        plan = None

        if request.user.profile.plan == "Premium":
            plan = PlanPremium(request, form)

        if request.user.profile.plan == "Enterprise":
            plan = PlanEnterprise(request, form)

        if plan == None or request.user.profile.plan == "Basic":
            plan = PlanBasic(request, form)

        plan.compute_fields()
        fields = plan.get_fields()

        return render(request, 'dapp/upload_image.html', {
            "user_data": request.user,
            "profile_data": request.user.profile,
            "form": form,
            "image_urls": True,
            **fields
        })

    else:
        form = UploadImageForm()

    return render(request, 'dapp/upload_image.html',
                  {"user_data": request.user,
                   "profile_data": request.user.profile,
                   "image_urls": False,
                   "form": form})
