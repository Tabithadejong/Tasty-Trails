from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, 'Draft'), (1, 'Published'))

class Recipe(models.Model): 
    two = 2 
    four = 4 
    six = 6 
    eight = 8 
    ten = 10 
    STARTER = 'Starter'
    MAIN = 'Main'
    DESSERT = 'Dessert'

    number_of_mouths = [ 
        (two, 2),
        (four, 4), 
        (six, 6),
        (eight, 8),
        (ten, 10)
    ]
    
    category = [ 
        (STARTER , 'Starter'),
        (MAIN, 'Main'),
        (DESSERT, 'Dessert')
    ]

    recipe = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_post')
    cooking_time = models.TextField(name='cooking-time')
    amount_of_people = models.IntegerField(choices=number_of_mouths, default="" )
    catergory = models.CharField(max_length=100, choices=category, default= '')
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    ingriedents = models.TextField()
    preperation = models.TextField()
    image= CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)  

    class Meta:
        ordering = ['catergory']
        

    def __str__(self):
        return self.recipe
    
    def number_of_likes(self): 
        return self.likes.count()
            
        


