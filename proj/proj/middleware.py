import time
from django.http import HttpResponse
from django.shortcuts import render


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests = {}

    def __call__(self, request):
        if request.POST:
            ip = request.META.get('REMOTE_ADDR')
            if ip in self.requests:
                now = time.time()
                times = self.requests[ip]
                while times and times[0] < now - 60:
                    times.pop(0)
                if len(times) >= 3:
                    return render(request, 'dapp/upload_image.html', {
                        "user_data": request.user,
                        "profile_data": request.user.profile,
                        "upload_error": True})

            self.requests.setdefault(ip, []).append(time.time())
        response = self.get_response(request)
        return response