from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    if month  == "january":
        challenge_text = "Do strenthg training"
    elif month == "february":
        challenge_text = "Walk for atleast 45 min everyday!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 min everyday!"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)

