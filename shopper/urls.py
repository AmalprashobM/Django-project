from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.index,name='main'),
    path("item/<uuid:item_id>/", views.view_item,name = 'viewitem' ),
    path("search/",views.index,name='search'),
    path("add-cart/", views.add_cart),
    path("cart/", views.cart,name='cart'),
    path("delete-cart/", views.delete_cart),
    path("modify-item/", views.modify_cart),
    path("checkout/",views.checkout,name='checkout'),
    
]