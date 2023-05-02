
from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register(r'user', UserList)
router.register(r'question', QuestionList)

urlpatterns = [
    path('', include(router.urls)),
]