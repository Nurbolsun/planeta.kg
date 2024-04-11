from django.urls import path
from .views import PartAPIList, CategoryAPIList, RefCarMarkAPIList, RefCarModelAPIList

urlpatterns = [
    path('parts/', PartAPIList.as_view({'get': 'list'}), name='all-parts'),
    path('parts/<int:pk>', PartAPIList.as_view({'get': 'retrieve'})),
    path('parts/create/', PartAPIList.as_view({'post': 'create'})),

    path('category/', CategoryAPIList.as_view({'get': 'list'}), name='all-category'),
    path('category/<int:pk>', CategoryAPIList.as_view({'get': 'retrieve'})),
    path('category/create/', CategoryAPIList.as_view({'post': 'create'})),

    path('mark/', RefCarMarkAPIList.as_view({'get': 'list'}), name='all-marks'),
    path('mark/<int:pk>', RefCarMarkAPIList.as_view({'get': 'retrieve'})),
    path('mark/create/', RefCarMarkAPIList.as_view({'post': 'create'})),

    path('model/', RefCarModelAPIList.as_view({'get': 'list'}), name='all-model'),
    path('model/<int:pk>', RefCarModelAPIList.as_view({'get': 'retrieve'})),
    path('model/create/', RefCarModelAPIList.as_view({'post': 'create'})),
]