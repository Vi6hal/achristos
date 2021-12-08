from rest_framework.serializers import Serializer
from .serializers import RandomSerializer
from rest_framework import viewsets
from .models import RandomData

class RandomDataView(viewsets.ModelViewSet):
    queryset = RandomData.objects.all()
    serializer_class = RandomSerializer
