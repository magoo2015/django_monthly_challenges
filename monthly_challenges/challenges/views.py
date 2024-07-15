
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        
    except:
        return HttpResponseNotFound(f"<h1>This month is not supported</h1>")
