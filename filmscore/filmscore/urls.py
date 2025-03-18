from django.contrib import admin
from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from rest_framework.authtoken.views import obtain_auth_token
from rating.views import Movieviewset, Ratingviewset, RegisterUser, ProtectedView ,AddRatingView, MovieByTitleView


# Router Setup
router = DefaultRouter()  
router.register(r'movie', Movieviewset)  
router.register(r'rating', Ratingviewset) 


# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterUser.as_view(), name='register'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),  
    path('api/protected/', ProtectedView.as_view(), name='protected_view'),
    path('api/auth/', include('rest_framework.urls')),  
    path('api/add-rating/', AddRatingView.as_view(), name='add_rating'),
    path("api/movie/title/<str:title>/", MovieByTitleView.as_view(), name="movie-by-title"),
]