from rest_framework import authentication
import jwt_utils

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        JWToken = request.META.get('HTTP_JWTOKEN')
        if not JWToken:
            return None
        try:
            user = jwt_utils.get_user_from_token(JWToken)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('User Blocked')
        return user, None