from django.contrib import admin
from .models import *
# Register your models here.

class apartmentAdmin(admin.ModelAdmin):
    serviceTitle = ("roomSize","noofWindows","isMetro")

class villaAdmin(admin.ModelAdmin):
    serviceTitle = ("noOfRooms","carpetArea")

class employeeAdmin(admin.ModelAdmin):
    serviceTitle = ("empname","emp_age","emp_id","emp_department")

class restaurantAdmin(admin.ModelAdmin):
    serviceTitle = ("Menu", "noOfTable", "section", "price")




admin.site.register(Apartment,apartmentAdmin)
admin.site.register(Villa,villaAdmin)
admin.site.register(Employeedetails,employeeAdmin)
admin.site.register(Restaurant, restaurantAdmin)