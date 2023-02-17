from django.urls import path
from  . import views
app_name='shop'
urlpatterns = [

    path('',views.AllProdCat,name='AllProdCat'),
    path('<slug:cat_slug>',views.AllProdCat,name='products_by_category'),
    path('<slug:cat_slug>/<slug:prod_slug>/',views.ProdctDetails,name='ProdCatDetails'),
]
