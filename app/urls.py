from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('test', test, name='test'),
    path('search_tweet/', search_tweet, name="search_tweet"),
    path('test/view_tweets/', view_tweets, name="view_tweets"),
    path('documentation', documentation, name='documentation'),
    path('thread', thread, name='thread'),
    path('get_thread', get_thread, name='get_thread'),
    path('out-token', out_token, name="token"),
    path('subscription', subscribe, name='subscribe'),
    path('get_sub/<str:pk>', get_subscription, name="get_subscription"),
    path('add_token/<str:id>', add_token, name='add-token'),
    path('rephrase', rephrase, name='rephrase'),
    path('get_rephrase', rephrase_list, name='get_rephrase')
]
