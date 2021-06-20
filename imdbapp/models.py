from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Genre(models.Model):
    """This model will keep genre types
    For example:
    "Adventure", " Family", " Fantasy", " Musical"
    """
    name = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        ordering = ('id',)  # Maintain list order by id
        verbose_name_plural = "Genres"

    def __str__(self):
        return str(self.name)

def imdb_score_validation(imdb_score):
    # This function validate to make sure imdb_score greate tha 10
    if imdb_score >= 10.0:
        raise ValidationError('This is not a valid IMDB score, its value is always less than 10')

def popularity_validation(popularity):
    # This function validate to make sure popularity greate tha 10
    if popularity >= 100.0:
        raise ValidationError('This is not a valid popularity score, its value is always less than 100')

class Movie(models.Model):
    """This model will keep movie information,
    one movie will be associated many genre type
    and one genre will be associated with many movies"""
    name = models.CharField(blank=True, null=True, max_length=255,help_text='Related Org to associate with')
    director = models.CharField(blank=True, null=True, max_length=255,help_text='Related Org to associate with')
    genre = models.ManyToManyField(Genre,blank=True, null=True, max_length=255,help_text='Related Org to associate with')
    imdb_score = models.FloatField(blank=True, null=True, validators=[imdb_score_validation],help_text='Related Org to associate with')
    popularity = models.FloatField(blank=True, null=True, validators=[popularity_validation],help_text='Related Org to associate with')
    create_date = models.DateTimeField(null=True, blank=True,help_text='Related Org to associate with')
    edit_date = models.DateTimeField(null=True, blank=True,help_text='Related Org to associate with')

    class Meta:
        ordering = ('id',) # Maintain list by order
        verbose_name_plural = "Movies"

    def save(self, *args, **kwargs):
        # If create date is not give while creating model, it will save with current time
        if self.create_date is None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(Movie, self).save()

    def __str__(self):
        return str(self.name)