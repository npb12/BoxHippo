from django.contrib import admin
from listings.models import Listing, Category, SubCategory

admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(SubCategory)
