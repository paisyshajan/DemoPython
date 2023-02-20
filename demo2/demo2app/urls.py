from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),

    # path('register/',views.register,name='register')



    # path('add/',views.addition,name='addtn')




    # path('about/',views.about,name='about'),
    # path('contact',views.contact,name='contact')
]
