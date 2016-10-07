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
    context = {
        "all_movies": Item.objects.all()


    }
    return render(request, "movies.html", context)


def rater_view(request):
    context = {
        "raters": Rater.objects.all()


    }
    return render(request, "rater.html", context)


def user_info(request, rater_id):
    context = {
        "user": Rater.objects.get(id=rater_id),
        "movies": Data.objects.filter(rater=rater_id)

    }
    return render(request, "user.html", context)
