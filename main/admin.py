from django.contrib import admin
from .models import Articles, CustomUser, Comments

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'text']



class CommentsAdmin(admin.ModelAdmin):
    list_display = [ 'text']       

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(CustomUser)