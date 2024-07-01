# myapp/middleware.py

import uuid
import time
from django.conf import settings
from django.http import JsonResponse


class VerificationStringMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process request before view is called
        generated_key = request.headers.get('X-G-Key')
        timestamp = request.headers.get('X-Timestamp')
        uuid_str = request.headers.get('X-UUID')
        shared_key = settings.SHARED_KEY


        if not (generated_key and timestamp and uuid_str):
            return JsonResponse({'error': 'Missing required headers'}, status=400)

        x = XORhash(shared_key)
        x1 = XORhash(str(timestamp))
        x2 = XORhash(uuid_str)
        expected_verification_string = x * x * x1 * x1 * x2 * x2 * 11

        # Compare received generated key with expected one
        if generated_key != str(expected_verification_string):
            s = f"error: Invalid generated key == {expected_verification_string}"
            return JsonResponse(s, status=400)

        # Pass control to the next middleware or view
        response = self.get_response(request)

        # Process response after view is called

        return response

def XORhash(key):
    hash_value = 0
    for char in key:
        hash_value ^= ord(char)
    if hash_value == 0:
        return 7
    return hash_value

#  x = XORhash(shared_key)
# x1 = XORhash(str(timestamp))
# x2 = XORhash(uuid_str)
# expected_verification_string = x * x * x1 * x1 * x2 * x2 * 11