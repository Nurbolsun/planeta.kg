from django.urls import path
from .views import PartAPIList

urlpatterns = [
    path('parts/', PartAPIList.as_view({'get': 'list'}), name='all-parts'),

]