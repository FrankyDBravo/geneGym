from django.db import models

# Create your models here.

class muscle():

    muscle_id = models.ForeignKey( )
    name = models.CharField()
    is_front = models.BooleanField()
    image_url_main =  models.URLField()
    image_url_secondary =  models.URLField()


class exercise():

    id = models.IntegerField(primary_key=True)
    uuid = models.CharField()
    name = models.CharField()
    status	= models.CharField()
    description	 = models.CharField()
    creation_date	= models.DateField()
    category = models.ForeignKey()
    language = models.ForeignKey()
    images = models.URLField()
    license	= models.CharField
    license_author	= models.CharField

class exerciseImage():

    exercise_id = models.ForeignKey( )
    image = models.URLField()
    isMain = models.BooleanField()

class exerciseVariation():
    
    exercise_id = models.ForeignKey( )
    exercise_variation_id = models.ForeignKey( )

class exercise2muscle():

    exercise_id = models.ForeignKey( )
    muscle_id = models.ForeignKey()

class exercise2muscleSecondary():

    exercise_id = models.ForeignKey( )
    muscle_id = models.ForeignKey()

class exercise2equipment():

    exercise_id = models.ForeignKey( )
    equipment_id = models.ForeignKey( )
