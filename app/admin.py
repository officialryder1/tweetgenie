from django.contrib import admin
from .models import Tweets, UserToken, Subscription, user_subscription

admin.site.register(Tweets)
admin.site.register(UserToken),
admin.site.register(Subscription),
admin.site.register(user_subscription),
