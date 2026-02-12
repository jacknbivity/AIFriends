from django.urls import path, re_path

from web.models.user import UserProfile
from web.views.character.remove import RemoveCharacterView
from web.views.character.update import UpdateCharacterView
from web.views.character.get_single import GetSingleCharactorView
from web.views.character.create import CreateCharacterView
from web.views.index import index
from web.views.user.account.get_user_info import GetUserInfo
from web.views.user.account.login import LoginAPIView
from web.views.user.account.logout import LogoutView
from web.views.user.account.refresh_token import RefreshTokenView
from web.views.user.account.register import RegisterAPIView
from web.views.user.profile.upadate import UpdateProfileView

urlpatterns = [
    path('api/user/account/login/', LoginAPIView.as_view()),
    path('api/user/account/logout/', LogoutView.as_view()),
    path('api/user/account/register/', RegisterAPIView.as_view()),
    path('api/user/account/refresh_token/', RefreshTokenView.as_view()),
    path('api/user/account/get_user_info/', GetUserInfo.as_view()),
    path('api/user/profile/update/', UpdateProfileView.as_view()),

    path('api/create/character/create/', CreateCharacterView.as_view()),
    path('api/create/character/update/', UpdateCharacterView.as_view()),
    path('api/create/character/remove/', RemoveCharacterView.as_view()),
    path('api/create/character/get_single/', GetSingleCharactorView.as_view()),

    path('', index),
    re_path(r'^(?!media/|static/|assets/).*$', index)  ## 兜底路由
]
