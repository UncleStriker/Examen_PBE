from django.urls import path, include
from rest_framework import routers
from usuarios import views


router = routers.DefaultRouter()

router.register(r'User', views.UserViewSet)
router.register(r'Topico', views.TopicoViewSet)
router.register(r'Post', views.PostViewSet)


urlpatterns = [
    path('', include(router.urls))
]
