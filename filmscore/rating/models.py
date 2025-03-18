from django.db import models
from django.contrib.auth.models import User
class Movie(models.Model):  
    title=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    release_date=models.DateField()

    def __str__(self):
        return self.title

class Rating(models.Model):  
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField(blank=True, null=True)
    class Meta:
         unique_together = [['user', 'movie']]  
    
    def __str__(self):
        return f"  {self.user.username} - {self.movie.title} - {self.stars} stars"