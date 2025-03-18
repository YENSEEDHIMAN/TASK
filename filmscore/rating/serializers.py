from rest_framework import serializers
from .models import Movie, Rating

class Ratingserializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = '__all__'

    def get_average_rating(self, obj):
        """Calculate the average rating of the movie"""
        movie = obj.movie  # Get the associated movie
        ratings = movie.ratings.all()  # Get all ratings for the movie
        
        if ratings.exists():  
            return sum(r.stars for r in ratings) / ratings.count()
        return 0  # Default if no ratings


class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "release_date"]  

