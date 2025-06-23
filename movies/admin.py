from django.contrib import admin

from .models import Movie, Review, Genre

@admin.register(Movie)
class PosterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Review)
admin.site.register(Genre)
