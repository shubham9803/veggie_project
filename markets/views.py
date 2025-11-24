from rest_framework import generics
from .models import Market
from .serializers import MarketSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MarketListCreateView(generics.ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MarketRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
