from django.contrib import admin
from .models import Cars, Rent


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('registration', 'name', 'model', 'year', 'cc', 'image')

    search_fields = ('name', 'model')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Cars, CarAdmin)


class RentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'second_name', 'telephone', 'registration', 'from_date', 'to_date', 'period', 'picked',
        'returned')

    search_fields = ('first_name', 'registration')
    #prepopulated_fields = {'slug':('name',)}


admin.site.register(Rent, RentAdmin)
