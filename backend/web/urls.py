from django.urls import path

from web.views.index import index
from web.views.user.account.login import LoginAPIView
from web.views.user.account.logout import LogoutView
from web.views.user.account.refresh_token import RefreshTokenView
from web.views.user.account.register import RegisterAPIView

urlpatterns = [
    path('api/user/account/login/', LoginAPIView.as_view()),
    path('api/user/account/logout/', LogoutView.as_view()),
    path('api/user/account/register/', RegisterAPIView.as_view()),
    path('api/user/account/refresh_token/', RefreshTokenView.as_view()),
    path('', index)
]
