from django.contrib import admin
from .models import Person , SubDistrict , District , Division , Country
# Register your models here.
admin.site.register(Person)
admin.site.register(SubDistrict)
admin.site.register(District)
admin.site.register(Division)
admin.site.register(Country)