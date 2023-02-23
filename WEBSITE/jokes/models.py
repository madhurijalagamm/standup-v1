
from django.db import models

class JOKES(models.Model):
    joke_text = models.CharField(max_length=100)
    upvote = models.IntegerField()
    downvote = models.IntegerField()

    # published_date = models.DateField()

    def __str__(self):
        return f"{self.joke_text} has {self.upvote} upvotes"