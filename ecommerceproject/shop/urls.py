from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.view_cart, name='cart'),
    path('payments/', views.payments, name='payments'),
    path('signup/', views.signup_user, name='signup'),
    path('signin/', views.signin_user, name='signin'),
    path('signout/', views.signout_user, name='signout'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('<slug:slug_c>/', views.home, name='products_by_category'),
    path('<slug:slug_c>/<slug_p>/', views.prod_details, name='prod_details'),

]

