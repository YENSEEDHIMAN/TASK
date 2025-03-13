from django.urls import path
from .views import UserRegistrationView, UserLoginView, ProfileView ,UserchangePasswordView 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"), 
    path("changepassword/", UserchangePasswordView.as_view(), name="changepassword"), 
   
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

