from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'email',
        'shipping_address',
        'billing_address',
        'nickname',
    )


admin.site.register(Customer, CustomerAdmin)
