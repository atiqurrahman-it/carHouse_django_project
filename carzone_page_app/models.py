from django.db import models


# Create your models here.

class Teams(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='team_pic/')  # Y%/m%/d%/ folder create with time date year
    facebook_url = models.URLField()
    twitter = models.URLField()
    google_plus_url = models.URLField()
    create_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
