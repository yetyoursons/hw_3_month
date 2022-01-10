
from django.contrib import admin
from django.urls import path
from shop import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/',views.category_list_view),
    path('api/v1/tags/',views.tag_list_view),
    path('api/v1/products/<int:id>/',views.product_list_view),
    path('api/v1/products/<int:id>/',views.review_detail_view),
]
