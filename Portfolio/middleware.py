# myproject/middleware/admin_ip_middleware.py
# myapp/middleware.py

from django.http import HttpResponseForbidden
from decouple import config as Config


class CustomURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define the URL paths you want to restrict
        restricted_paths = ['/admin/', '/sgadmin/']  # Add your desired restricted paths

        if request.path in restricted_paths:
            # Check if the request comes from an allowed IP address
            allowed_ips = [Config('IP'),]  # Replace with your allowed IP addresses

            user_ip = request.META.get('REMOTE_ADDR')
            print(user_ip)
            if user_ip not in allowed_ips:
                return HttpResponseForbidden("You are not allowed to access this URL.")

        response = self.get_response(request)
        return response
