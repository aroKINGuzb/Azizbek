from django.contrib import admin
from .models import News,Category
class NewsAdmin(admin.ModelAdmin):
    # list_filter = ["title", "description",'category']
    list_display=["title", "description",'category']

admin.site.register(Category)
admin.site.register(News,NewsAdmin)
