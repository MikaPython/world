from django.contrib import admin

from .models import *

class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 10


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'user', 'updated', )
    inlines = [ImageInlineAdmin, ]


admin.site.register(Category)


