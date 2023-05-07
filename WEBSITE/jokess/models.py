
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class JOKES(models.Model):
    slug = models.SlugField(null=True)
    joke_text = models.CharField(max_length=255)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    author = models.CharField(max_length=255)
    # published_date = models.DateField()

    # def __str__(self):
    #     return f"{self.joke_text} has {self.upvote} upvotes"
    def __str__(self):
        return self.joke_text

    def get_absolute_url(self):
        return reverse("seejokes3", kwargs={"slug": self.slug})
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.joke_text)
    #     super().save(*args, **kwargs)