from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


monthly_challenges_dict = {
    "january": "Go to GYM everyday",
    "february": "Freedom is on the other side of Discipline",
    "march": "We have to sacrifice either sleep or dreams",
    "april": "Dreams are not made in comfort zone",
    "may": "May is beutiful month",
    "june": "Make love, people do not survive without it",
    "july": "How much money man needs to be happy, just one more dollar",
    "august": "just chill",
    "september": "Learn technical things with good learning rate",
    "october": "Become the data scientist in finance domain",
    "november": "Need to have good grasp over the linear algebra, calculus and probability and statistics",
    "december": "it is a continuous process"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges_dict.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}<\a></li>"
    response_data = f"<ul>{list_items}<ul>"
    return HttpResponse(response_data)


def monthly_challenges_number(request, month):
    months = list(monthly_challenges_dict.keys())
    redirect_month = months[(month - 1) % 12]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    # monthly_challenge = monthly_challenges_dict[month]
    try:
        monthly_challenge = monthly_challenges_dict[month]
        response_data = f"<h1>{monthly_challenge}<h2>"
        return HttpResponse(render_to_string("challenges/challenge.html"))
    except:
        return HttpResponseNotFound("This month is not supported!")




