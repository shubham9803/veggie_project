from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Rate
from .serializers import RateSerializer

class RateListCreateView(generics.ListCreateAPIView):
    queryset = Rate.objects.all().order_by('-created_at')
    serializer_class = RateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class RateRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [IsAuthenticated]


# Admin verify endpoint
from rest_framework.views import APIView

class VerifyRateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            rate = Rate.objects.get(pk=pk)
        except Rate.DoesNotExist:
            return Response({"detail": "Rate not found"}, status=404)

        if request.user.profile.role != "admin":
            return Response({"detail": "Only admin can verify"}, status=403)

        rate.is_verified = True
        rate.verified_by = request.user
        rate.save()

        return Response({"detail": "Rate verified successfully"})
