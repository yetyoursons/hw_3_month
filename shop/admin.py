from django.contrib import admin
from . models import Category
from . models import Tag
from . models import Product
from . models import Review
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Review)
