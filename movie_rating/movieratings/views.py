from django.shortcuts import render
from django.http import HttpResponse
from movieratings.models import Item, Data, Rater
from django.db.models import Avg


def index_view(request):
    context = {
        "top_20": Item.objects.all()



    }
    return render(request, "start.html", context)
    # return HttpResponse("This is the Movie Rating Homepage!")


def movie_view(request):
    return render(request, "movies.html")
