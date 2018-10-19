from django.contrib import admin
from .models import Profile, City, Country


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthday', 'user_country', 'user_city', )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)


# Register your models here.
