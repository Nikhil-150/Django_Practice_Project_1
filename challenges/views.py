from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    "december": None
}


def index(request):
    months = list(monthly_challenges_dict.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_number(request, month):
    months = list(monthly_challenges_dict.keys())
    redirect_month = months[(month - 1) % 12]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    # monthly_challenge = monthly_challenges_dict[month]
    try:
        monthly_challenge = monthly_challenges_dict[month]
        return render(request, "challenges/challenge.html", {
            "text": monthly_challenge,
            "month_name": month,

        })
        # response_data = f"<h1>{monthly_challenge}<h2>"
        # return HttpResponse(render_to_string("challenges/challenge.html"))
    except:
        response_data = render_to_string("404.html")
        raise Http404(response_data)




