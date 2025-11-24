from rest_framework import generics
from .models import Vegetable
from .serializers import VegetableSerializer

class VegetableListCreateView(generics.ListCreateAPIView):
    queryset = Vegetable.objects.all()
    serializer_class = VegetableSerializer


class VegetableRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vegetable.objects.all()
    serializer_class = VegetableSerializer
