from django.db import models
from django.contrib.auth.models import User

class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.PositiveIntegerField(default=25)
    
    def __str__(self):
        return str(self.user) + ' - ' + ' has ' + str(self.token) + ' remaining' 

class Tweets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_title = models.CharField(max_length=200)
    tweet = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.tweet_title
    
class Subscription(models.Model):
    name = models.CharField(max_length=20)
    amount = models.PositiveIntegerField()
    token = models.IntegerField()
    package = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    

class user_subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_type = models.OneToOneField(Subscription, on_delete=models.CASCADE, related_name='user_plan')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return str(self.user) + ' Plan: ' + str(self.plan_type)