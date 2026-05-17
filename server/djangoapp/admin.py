from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class allows adding CarModel records directly inside the CarMake page
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2  # Provides 2 extra blank slots by default to quickly add new models

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')
    list_filter = ['type', 'year']
    search_fields = ['name']

# CarMakeAdmin class with CarModelInline embedded
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)