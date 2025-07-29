from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=122)
    desc = models.CharField(max_length=500)
    date = models.DateField(default= timezone.now)
    img = models.ImageField(upload_to="img/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=122, blank=True)
    profile_pic = models.ImageField(upload_to="img/")

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    




