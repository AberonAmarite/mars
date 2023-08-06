from django.urls import path
from . import views

urlpatterns = [
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('create_item/', views.create_item, name='create_item'),
    path('update_item/<int:pk>/', views.update_item, name='update_item'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
    path('get_item_details/', views.get_item_details, name='get_item_details'),
]