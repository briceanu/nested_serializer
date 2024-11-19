from django.urls import path
from . import views

urlpatterns =[
    path('create',views.PostTruckModelAPI.as_view(),name='create'),
    path('create_owner',views.CreateOwnerAPI.as_view(),name='create_owner'),
    # path('extra_data',views.ExtraDataAPI.as_view(),name='extra_data')

    
    ]