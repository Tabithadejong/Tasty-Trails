from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin 


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin): 

    prepopulated_fields = {'slug' : ('recipe', )}
    list_filter = ('status', 'category', 'created_on')
    search_fields = ['amount_of_people', 'recipe']
    list_display = ('recipe', 'status', 'cooking_time', 'created_on')
    summernot_fields = ('content')

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin): 

    list_display = ('name', 'context', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'context')
    actions = [ 'approve_comments']

    def approve_comments(self, request, queryset): 
        queryset.update(apporoved=True)

        

