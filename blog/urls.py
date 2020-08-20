from rest_framework.routers import DefaultRouter
from blog import views
from django.urls import path, include

router = DefaultRouter()
router.register('products', views.UserViewSet, basename='products-list')
router.register('register', views.UserCreate, basename='register')

urlpatterns =[
			path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]+router.urls