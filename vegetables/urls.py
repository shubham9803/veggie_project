from django.urls import path
from .views import VegetableListCreateView, VegetableRetrieveUpdateDeleteView

urlpatterns = [
    path('', VegetableListCreateView.as_view(), name='vegetable-list-create'),
    path('<uuid:pk>/', VegetableRetrieveUpdateDeleteView.as_view(), name='vegetable-detail'),
]
