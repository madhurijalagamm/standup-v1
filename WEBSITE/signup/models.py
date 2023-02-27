
from django.db import models

class USER(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)


    # published_date = models.DateField()

    # def __str__(self):
    #     return f"{self.joke_text} has {self.upvote} upvotes"