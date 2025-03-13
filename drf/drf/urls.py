
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from regform.views import home, RegisterUserView 

urlpatterns = [
    # path('', home, name='home'),  
    # path('register/', RegisterUserView.as_view(), name='register'), 
    path('api/user/', include('regform.urls')),  
    path('admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)