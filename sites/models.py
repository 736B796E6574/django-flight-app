from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class FlyingSite(models.Model):
    site_name = models.CharField(max_length = 150, unique=True)
    wind_direction = models.CharField(max_length = 150, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    pilot = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flying_sites")
    updated_on = models.DateTimeField(auto_now=True)
    overview = models.TextField()
    landing_information = models.TextField()
    warnings = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices = STATUS, default = 0)
    likes = models.ManyToManyField(User, related_name= "site_likes", blank = "true")
    
    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.like.count()

class Comment(models.Model):
    pilot = models.ForeignKey(FlyingSite, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100, default="Unknown Pilot")
    email = models.EmailField(default="pilot@pilot.com")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

class Photos(models.Model):
    taken_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photos")
    site_name = models.CharField(max_length = 150, unique=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.like.count()

