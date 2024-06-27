from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat no meat",
    "february": "Walk for at least 20 min",
    "march": "Learn Django for at least 20 min everyday",
    "april": "Try to survive",
    "may": "Run a 5k",
    "june": "See a maverick game",
    "july": "Build soccer website",
    "august": "Run a 5k",
    "september": "See a maverick game",
    "october": "Build soccer website",
    "november": "Eat no meat",
    "december": "Walk for at least 20 min",
}
# Create your views here.

def monthly_challenge_by_number(request, month):
    months= list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
        
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
    

