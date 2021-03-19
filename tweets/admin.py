from django.contrib import admin

from tweets.models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['timestamp','tip','author','published']
    


