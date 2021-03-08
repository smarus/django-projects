from django.contrib import admin


class FilmAdmin(admin.ModelAdmin):
    readonly_fields = ['writer', 'director']