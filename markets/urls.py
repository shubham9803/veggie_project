from django.urls import path
from .views import MarketListCreateView, MarketRetrieveUpdateDeleteView

urlpatterns = [
    path('', MarketListCreateView.as_view(), name='market-list-create'),
    path('<uuid:pk>/', MarketRetrieveUpdateDeleteView.as_view(), name='market-detail'),
]
