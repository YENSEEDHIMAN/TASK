from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Movie, Rating
from .serializers import Movieserializer, Ratingserializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
import urllib.parse  

class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"message": "User created successfully", "token": token.key}, status=status.HTTP_201_CREATED)

class AddRatingView(APIView):
    permission_classes = [IsAuthenticated]  

    def post(self, request):
        movie_id = request.data.get("movie")
        stars = request.data.get("stars")
        review = request.data.get("review", "")

        if not movie_id or not stars:
            return Response({"error": "Movie ID and stars are required"}, status=status.HTTP_400_BAD_REQUEST)

        movie = get_object_or_404(Movie, id=movie_id)

        rating, created = Rating.objects.update_or_create(
            movie=movie, user=request.user, 
            defaults={"stars": stars, "review": review}
        )

        return Response(Ratingserializer(rating).data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

class ProtectedView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        return Response({"message": "You are authenticated!", "user": request.user.username})

class Movieviewset(ModelViewSet):
    queryset = Movie.objects.prefetch_related('ratings').all()
    serializer_class = Movieserializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def head(self, request, *args, **kwargs):
        response = Response()
        response['Total-Movies'] = Movie.objects.count()  # Custom header
        response['Content-Type'] = 'application/json'  # Ensure correct content type
        return response
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class MovieByTitleView(APIView):
    def get(self, request, title):
        decoded_title = urllib.parse.unquote(title)
        movies = Movie.objects.filter(title=decoded_title)

        if not movies.exists():
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Movieserializer(movies, many=True)  # Serialize multiple results
        return Response(serializer.data, status=status.HTTP_200_OK)

class Ratingviewset(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = Ratingserializer
    permission_classes = [IsAuthenticatedOrReadOnly]

   
