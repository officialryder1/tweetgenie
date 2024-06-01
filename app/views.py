from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from replicate.client import Client
from .models import Tweets, UserToken, Subscription, user_subscription
from django.contrib import messages


client = Client(api_token=settings.REPLICATE_API_TOKEN)




def home(request):
  subscription = Subscription.objects.all()
  content = {
    'sub':subscription
  }
  return render(request, 'app/index.html', content)
  

@login_required(login_url='login_user')
def test(request):

  if UserToken.objects.filter(user=request.user).exists():
    user = UserToken.objects.get(user=request.user)
    return render(request, 'app/test.html', {'user':user})
  else:
    token = UserToken.objects.create(user=request.user)
    user = UserToken.objects.get(user=request.user)
    return render(request, 'app/test.html', {'user':user})
  
@login_required(login_url='login_user')
def search_tweet(request):
  token = UserToken.objects.get(user=request.user)
  tweet = request.POST.get('tweet')

  
  if token.token == 0:
    messages.success(request, ("You are out of wishes!"))
    return redirect('token')
  else:
    stream = client.stream(
      ref = "meta/meta-llama-3-70b-instruct",
      input={
          "top_k": 0,
          "top_p": 0.9,
          "prompt": "make a twitter tweet just the tweet and no intro, about " + tweet,
          "max_tokens": 512,
          "min_tokens": 0,
          "temperature": 0.6,
          "system_prompt": "You are a helpful assistant",
          "length_penalty": 1,
          "stop_sequences": "<|end_of_text|>,<|eot_id|>",
          "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
          "presence_penalty": 1.15,
          "log_performance_metrics": False
      },
      
    )
    
  
    print(stream)
    full_response = []
    for chunk in stream:
      full_response.append(chunk)


    output_respond = []
    for output in full_response:
      output_respond.append(output)

    tweet = Tweets.objects.create(user=request.user, tweet_title=tweet, tweet=output_respond)
    token = UserToken.objects.get(user=request.user)
    token.token -= 1
    token.save()
    return render(request, 'partials/tweet_list.html', {'event':full_response})
  

@login_required(login_url='login_user')
def view_tweets(request):
  tweet = Tweets.objects.all()
  content = {
    'tweet':tweet
  }
  return render(request, 'partials/tweets.html', content)

def thread(request):
  return render(request, 'app/thread.html', {})

def get_thread(request):
  tweet = request.POST.get('tweet')

  stream = client.stream(
    ref = "meta/meta-llama-3-70b-instruct",
     input={
        "top_k": 0,
        "top_p": 0.9,
        "prompt": "make a twitter thread just the thread and no intro, about " + str(tweet),
        "max_tokens": 512,
        "min_tokens": 0,
        "temperature": 0.6,
        "system_prompt": "You are a helpful assistant",
        "length_penalty": 1,
        "stop_sequences": "<|end_of_text|>,<|eot_id|>",
        "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "presence_penalty": 1.15,
        "log_performance_metrics": False
     },
    
  )

  full_response = []
  for chunk in stream:
    full_response.append(chunk)

  output_respond = []
  for output in full_response:
    output_respond.append(output)

  tweet = Tweets.objects.create(user=request.user, tweet_title=tweet, tweet=output_respond)
  token = UserToken.objects.get(user=request.user)
  token.token -= 5
  token.save()
  return render(request, 'partials/thread_list.html', {'event':full_response} )

def documentation(request):
  return render(request, 'app/documentation.html', {})

@login_required(login_url='login_user')
def out_token(request):
  subscription = Subscription.objects.all()
  content = {
    'sub':subscription
  }
  return render(request, 'partials/out_token.html', content)

@login_required(login_url='login_user')
def subscribe(request):
  subscription = Subscription.objects.all()
  content = {
    'sub':subscription
  }
  return render(request, 'partials/subscribe.html', content)

@login_required(login_url='login_user')
def get_subscription(request, pk):
  sub = Subscription.objects.get(pk=pk)
  content  = {
    'sub':sub
  }
  return render(request, 'partials/get_sub.html', content)

@login_required(login_url='login_user')
def add_token(request, id):
  sub = Subscription.objects.get(id=id)
  user = UserToken.objects.get(user=request.user)
  user.token += sub.token
  user.save()
  return redirect('test') 

@login_required(login_url='login_user')
def rephrase(request):
  return render(request, 'app/rephrase.html', {})

@login_required(login_url='login_user')
def rephrase_list(request):
  tweet = request.POST.get('tweet')

  stream = client.stream(
    ref = "meta/meta-llama-3-70b-instruct",
     input={
        "top_k": 0,
        "top_p": 0.9,
        "prompt": "rephrase this tweet for me, just the rephrase no intro " + str(tweet),
        "max_tokens": 512,
        "min_tokens": 0,
        "temperature": 0.6,
        "system_prompt": "You are a helpful assistant",
        "length_penalty": 1,
        "stop_sequences": "<|end_of_text|>,<|eot_id|>",
        "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "presence_penalty": 1.15,
        "log_performance_metrics": False
     },
    
  )

  full_response = []
  for chunk in stream:
    full_response.append(chunk)

  output_respond = []
  for output in full_response:
    output_respond.append(output)

  tweet = Tweets.objects.create(user=request.user, tweet_title=tweet, tweet=output_respond)
  token = UserToken.objects.get(user=request.user)
  token.token -= 2
  token.save()
  return render(request, 'partials/rephrase_list.html', {'event':full_response} )

def next(request):
  pass