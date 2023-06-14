from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing_detail, name='listing'),
    path('<int:listing_id>/pdf', views.GeneratePDF.as_view(), name='pdf_listing'),
    path('search', views.search, name='search'),
]
