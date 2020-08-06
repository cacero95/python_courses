from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello_viewset', views.HelloViewSet, basename="hello_viewset")
router.register('profile', views.UserProfileViewSet),
router.register('login', views.LoginViewSet, basename='login')
urlpatterns = [
    url(r'^hello_view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]