from django.urls import path
from .views import CheckUser, CustomAuthToken, RegisterView,ChangePasswordView,UpdateProfileView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/',CustomAuthToken.as_view(),name="login"),
    path('check/user/',CheckUser.as_view(),name='check_user'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='update_profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)