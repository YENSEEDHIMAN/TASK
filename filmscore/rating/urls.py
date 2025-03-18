from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import Movieviewset, Ratingviewset ,RegisterUser

router = DefaultRouter()  
router.register(r'movie', Movieviewset)  
router.register(r'rating', Ratingviewset)  

urlpatterns = [
    path('api/', include(router.urls)),  

    
   
]
