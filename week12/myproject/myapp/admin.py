from django.contrib import admin

from myapp.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','fullname','address','postcode','email']
admin.site.register(Customer, CustomerAdmin)
