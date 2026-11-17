from ..jwt import decode_token
from django.contrib.auth import get_user_model


User = get_user_model()
class AuthenticationVerify:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        auth_header = request.headers.get('Authorization')

        if ( auth_header and auth_header.startswith('Bearer ')):
            token = auth_header.split(' ')[1]
            payload = decode_token(token)


            if payload:
                try:
                    request.user = User.objects.get(id = payload['user_id'])
                except User.DoesNotExist:
                    request.user = None
        return self.get_response(request)