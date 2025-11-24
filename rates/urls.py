from django.urls import path
from .views import (
    RateListCreateView,
    RateRetrieveUpdateDeleteView,
    VerifyRateView
)

urlpatterns = [
    path('', RateListCreateView.as_view(), name='rate-list-create'),
    path('<uuid:pk>/', RateRetrieveUpdateDeleteView.as_view(), name='rate-detail'),
    path('<uuid:pk>/verify/', VerifyRateView.as_view(), name='rate-verify'),
]
