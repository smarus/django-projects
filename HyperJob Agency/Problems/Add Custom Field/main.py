from django.contrib import admin


class FilmAdmin(admin.ModelAdmin):
    fields = ['creation_year']
    readonly_fields = ['creation_year']

    def creation_year(self, obj):
        return obj.year
