from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField



# model for adding recipes 

status = ((0, 'Draft'), (1, 'Published'))

class Recipe(models.Model): 
    two = 2 
    four = 4 
    six = 6 
    eight = 8 
    ten = 10 
    STARTER = 'Starter'
    MAIN = 'Main'
    DESSERT = 'Dessert'
    SHORT = '30 - 60 minutes' 
    REGULAR =  '1 hour - 2 hour' 
    LONG = '2 hours - 3 hours'
    

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
    time = [ 
        (SHORT , '30 - 60 minutes'), 
        (REGULAR ,  '1 hour - 2 hour'), 
        (LONG ,  '2 hours - 3 hours'), 
    ]

    recipe = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_post')
    cooking_time = models.CharField(max_length=100, choices=time, default="")
    amount_of_people = models.IntegerField(choices=number_of_mouths, default="" )
    category = models.CharField(max_length=100, choices=category, default= '')
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    ingriedients = models.TextField()
    preperation = models.TextField()
    image= CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=status, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)  

    class Meta:
        ordering = ['category']
        

    def __str__(self):
        return self.recipe
    
    def number_of_likes(self): 
        return self.likes.count()



class Comment(models.Model): 

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    context = models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)   


    def __str__(self):
        return self.name
    
    def number_of_likes(self): 
        return self.likes.count()
  


