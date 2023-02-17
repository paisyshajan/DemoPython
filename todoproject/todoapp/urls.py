
from django.urls import path

from .import views
app_name='todoapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),


    path('listview/', views.TaskListView.as_view(), name='listview'),
    path('detailsview/<int:pk>/', views.TaskDetailView.as_view(), name='detailsview'),    #DetailView must be 'pk' rather than 'id'
    path('updateview/<int:pk>/',views.TaskUpdateView.as_view(),name='updateview'),
    path('deleteview/<int:pk>/', views.TaskDeleteView.as_view(), name='deleteview'),


    # path('details',views.details,name='details')

]
