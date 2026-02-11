from django.urls import path
from .views import product_list, about_page, product_detail, register_view, login_view, logout_view, view_cart, add_to_cart, update_cart_item, remove_from_cart, create_payment, payment_success


urlpatterns = [
    path('', product_list, name='product_list'),
    path('about/', about_page, name='about_page'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/update/<int:product_id>/', update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('pay/<int:product_id>', create_payment, name='create_payment'),
    path('payment_success/', payment_success, name='payment_success')
]