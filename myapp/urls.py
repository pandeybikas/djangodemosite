from django.urls import path
from. import views
app_name= 'myapp'
urlpatterns = [
    path('', views.index, name='home'),
    path('products', views.products, name='products'),
    path('products/<int:pk>', views.ProductDeatilView.as_view(), name= 'producr_detail'),
    path('products/add', views.ProductCreateView.as_view(), name='add_product'),
    path('products/update/<int:pk>', views.ProductUpdateView.as_view(), name= 'update_product'),
    path('products/delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('seller_detail/<int:id>', views.seller_detail, name= 'seller_detail'),
    path('products/mylisting', views.seller_listing, name='mylisting')
]
