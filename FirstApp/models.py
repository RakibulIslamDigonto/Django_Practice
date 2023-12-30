from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    

class Album(models.Model):
    artist_name = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = (
        (1, "Worst"),
        (2, "Not good"),
        (3, "good"),
        (4, "Better"),
        (5, "Best"),
    )
    num_stars = models.IntegerField(choices=rating)

    def __str__(self) -> str:
        return self.album_name




