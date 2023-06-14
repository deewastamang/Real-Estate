from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contacts'),
    path('<int:id>', views.contact_delete, name='delete_contact'),
]
