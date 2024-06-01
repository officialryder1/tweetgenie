from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('search_tweet/', views.search_tweet, name="search_tweet"),
    path('test/view_tweets/', views.view_tweets, name="view_tweets"),
    path('documentation', views.documentation, name='documentation'),
    path('thread', views.thread, name='thread'),
    path('get_thread', views.get_thread, name='get_thread'),
    path('out-token', views.out_token, name="token"),
    path('subscription', views.subscribe, name='subscribe'),
    path('get_sub/<str:pk>', views.get_subscription, name="get_subscription"),
    path('add_token/<str:id>', views.add_token, name='add-token'),
    path('rephrase', views.rephrase, name='rephrase'),
    path('get_rephrase', views.rephrase_list, name='get_rephrase'),
    path('next', views.next, name='next')
]
