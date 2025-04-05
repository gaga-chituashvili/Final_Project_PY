from django.contrib import admin
from myapp.models import Product,Review
# Register your models here.

admin.site.register([Product])
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["name","price"]
    search_fields = ["name"]
    list_filter = ["name"]


admin.site.register(Review)

