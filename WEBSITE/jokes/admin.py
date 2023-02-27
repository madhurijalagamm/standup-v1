from django.contrib import admin
from jokes.models import JOKES

class JokeAdmin(admin.ModelAdmin):
    list_display=('joke_text','upvote','downvote')

admin.site.register(JOKES,JokeAdmin)

# Register your models here.
