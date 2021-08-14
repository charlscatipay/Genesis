from django.db import models

# Create your models here.
class UserProfile(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    date_of_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname}, {self.lastname}"

class UserCredential(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    user_profile = models.ForeignKey(UserProfile, null=True, on_delete=models.DO_NOTHING) #Last commit, null=True was added

    def __str__(self):
        return f"{self.username}"