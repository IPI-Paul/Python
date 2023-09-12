from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
# Django Rest Framework Token Authentication =>
  # keyword = 'Token' 
  keyword = 'Bearer' 
# <= Django Rest Framework Token Authentication
# JSON WEB Token Authentication with simplejwt =>
  # keyword = 'Token' 
# <= JSON WEB Token Authentication with simplejwt