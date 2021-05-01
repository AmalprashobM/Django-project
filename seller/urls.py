from django.urls import path,include
from . import views
urlpatterns = [
    path('create_shop/',views.create_shop),
    path("",views.index),
    path("shop/<uuid:shop_id>/add-item/", views.add_item),
     path("shop/<uuid:shop_id>/", views.view_shop),
    path("shop/<uuid:shop_id>/items/<uuid:item_id>/", views.view_item),
     path("shop/<uuid:shop_id>/orders/", views.vieworder),
]