from django.contrib import admin
from listings.models import Listing, Category, SubCategory, ProductPicture

admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProductPicture)
