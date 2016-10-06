from django.db import models


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    occupation = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=15)


class Item(models.Model):
    movie_title = models.CharField(max_length=150)
    release_date = models.CharField(max_length=30)
    video_release_date = models.CharField(max_length=50)
    imdb_url = models.CharField(max_length=150)
    unknown = models.BooleanField()
    action = models.BooleanField()
    adventure = models.BooleanField()
    animation = models.BooleanField()
    children = models.BooleanField()
    comedy = models.BooleanField()
    crime = models.BooleanField()
    documentary = models.BooleanField()
    drama = models.BooleanField()
    fantasy = models.BooleanField()
    film_noir = models.BooleanField()
    horror = models.BooleanField()
    musical = models.BooleanField()
    mystery = models.BooleanField()
    romance = models.BooleanField()
    sci_fi = models.BooleanField()
    thriller = models.BooleanField()
    war = models.BooleanField()
    western = models.BooleanField()

    def __str__(self):
        return self.movie_title


class Data(models.Model):
    rater = models.ForeignKey(Rater)
    item = models.ForeignKey(Item)
    rating = models.IntegerField()
    time_stamp = models.IntegerField()
