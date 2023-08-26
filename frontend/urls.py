from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.ListData.as_view(),name ="list_data"),
    path('add/', views.createData.as_view(),name ="add"),
     path('list2/', views.ListDataE.as_view(),name ="list_data2"),
    path('add2/', views.CreateDataE.as_view(),name ="add2"),
]
