import jwt
import warnings
from calendar import timegm
from datetime import datetime
import datetime as dt

from rest_framework_jwt.compat import get_username, get_username_field
from rest_framework_jwt.settings import api_settings
from . import models

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from django.db import IntegrityError
from django.contrib.auth import authenticate

# tapchiefabdc1243

def jwt_payload_handler(user):
	username_field = get_username_field()
	username = get_username(user)

	payload = {
		# 'user_id': user.pk,
		# 'email': user.email,
		'username': username,
		# 'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
		'exp': datetime.utcnow() + dt.timedelta(days=365),
	}

	payload[username_field] = username

	# Include original issued at time for a brand new token,
	# to allow token refresh
	if api_settings.JWT_ALLOW_REFRESH:
		payload['orig_iat'] = timegm(
			datetime.utcnow().utctimetuple()
		)

	return payload


def jwt_get_user_id_from_payload_handler(payload):
	"""
	Override this function if user_id is formatted differently in payload
	"""
	warnings.warn(
		'The following will be removed in the future. '
		'Use `JWT_PAYLOAD_GET_USERNAME_HANDLER` instead.',
		DeprecationWarning
	)

	return payload.get('user_id')


def jwt_get_username_from_payload_handler(payload):
	"""
	Override this function if username is formatted differently in payload
	"""
	return payload.get('username')


def jwt_encode_handler(payload):
	return jwt.encode(
		payload,
		api_settings.JWT_SECRET_KEY,
		api_settings.JWT_ALGORITHM
	).decode('utf-8')


def jwt_decode_handler(token):
	options = {
		# 'verify_exp': api_settings.JWT_VERIFY_EXPIRATION,
		'verify_exp': False,

	}

	return jwt.decode(
		token,
		api_settings.JWT_SECRET_KEY,
		api_settings.JWT_VERIFY,
		options=options,
		leeway=api_settings.JWT_LEEWAY,
		audience=api_settings.JWT_AUDIENCE,
		issuer=api_settings.JWT_ISSUER,
		algorithms=[api_settings.JWT_ALGORITHM]
	)


def jwt_response_payload_handler(token, user=None, request=None):
	"""
	Returns the response data for both the login and refresh views.
	Override to return a custom response such as including the
	serialized representation of the User.

	Example:

	def jwt_response_payload_handler(token, user=None, request=None):
		return {
			'token': token,
			'user': UserSerializer(user).data
		}

	"""
	return {
		'token': token
	}

def get_user_from_token(token):
	"""
	Utility function to get the user object from the token
	:type token: str
	:rtype: User
	"""
	username = jwt_get_username_from_payload_handler(jwt_decode_handler(token))
	try:
		user = (User.objects.get_by_natural_key(username))
		return user
	except User.DoesNotExist:
		raise ValueError("User does not exist for the given token")

def get_token_for_user(user):
	"""
	Utility to function to obtain a token for a user object, creates one if it does not exist
	:type user: User
	:rtype: str
	"""
	payload = jwt_payload_handler(user)
	value = jwt_encode_handler(payload)
	# models.UserJWToken.objects.create(user=user, token=value)
	return value

@api_view(['GET','POST'])
def get_token_with_password(request):
	print 'Hello from get_token_with_password'
	if request.method == 'POST':
		user = None
		try:
			user = authenticate(username=request.data['username'], password=request.data['password'])
		except:
			return Response({'id':-1, 'status': 'inaccurate input parameters'},status=status.HTTP_400_BAD_REQUEST)

		if user:
			if not user.is_active:
				msg = _('User account is disabled.')
				raise serializers.ValidationError(msg)

			# payload = jwt_payload_handler(user)
			token = get_token_for_user(user)

			# return {
			# 	# 'token': jwt_encode_handler(payload),
			# 	# 'user': user
			# 	'token': token
			# }

			# return Response({'id':1 ,'status': 'success'},{'token':token}, status=status.HTTP_201_CREATED)
			return Response({'token':token}, status=status.HTTP_201_CREATED)
		else:
			msg = _('Unable to login with provided credentials.')
			raise serializers.ValidationError(msg)
	return Response({'id':-1 ,'status': 'Only POST request supported'},status=status.HTTP_400_BAD_REQUEST)