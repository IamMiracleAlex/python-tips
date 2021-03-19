# from django.shortcuts import render
from django.views.generic import TemplateView


class TweetList(TemplateView):
    template_name = 'tweets/tweets.html'

    def get(self, request, *args, **kwargs):
        
        context = {
            'value': 0
        }
        return self.render_to_response(context)


def search(self, request):
    pass