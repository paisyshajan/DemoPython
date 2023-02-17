from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),





    # path('opertn/', views.operations, name='operation'),




    # path('contact/', views.contact, name='contact'),
    # path('details/', views.details, name='details'),
    # path('thanks', views.thanks, name='thanks'),

]
