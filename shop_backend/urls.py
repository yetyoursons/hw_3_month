
from django.contrib import admin
from django.urls import path
from shop import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', views.category_list_view),
    path('api/v1/products/<int:id>/', views.product_detail_view),
    path('api/v1/products/reviews/', views.product_review_view),
    path('api/v1/products/tags/', views.product_tag_view),
]
