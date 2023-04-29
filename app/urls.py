from django.urls import path
from .views import UserCreate, UserDetail, UserDelete


urlpatterns = [
    path('signup/', UserCreate.as_view()),
    path('users/<username>/', UserDetail.as_view()),
    path('close/', UserDelete.as_view())
]
