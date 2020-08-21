from rest_framework.routers import DefaultRouter
from blog import views
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register('products', views.UserViewSet, basename='products-list')
router.register('register', views.UserCreate, basename='register')

urlpatterns =[
			path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
			path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    		path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    		path('auth/', include('rest_framework_social_oauth2.urls')),
]+router.urls