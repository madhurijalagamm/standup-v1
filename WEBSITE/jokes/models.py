
from django.db import models

class JOKES(models.Model):
    joke_text = models.CharField(max_length=255)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    # published_date = models.DateField()

    # def __str__(self):
    #     return f"{self.joke_text} has {self.upvote} upvotes"