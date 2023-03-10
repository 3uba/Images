from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dapp.views import CustomLoginView
from dapp.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dapp.urls')),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='dapp/login.html',
                                           authentication_form=LoginForm), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
