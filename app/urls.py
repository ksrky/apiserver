from django.urls import path
from rest_framework import routers
from .views import UserViewSet, UserCreate, UserDetail, UserDelete

router = routers.DefaultRouter()
router.register('users/', UserViewSet)

urlpatterns = [
    path('signup/', UserCreate.as_view()),
    path('users/<username>/', UserDetail.as_view()),
    path('close/', UserDelete.as_view())
]
# router.registerl('users/<pk>', UserInfo)
# router.register('close/', UserDelete)
