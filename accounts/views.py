from rest_framework.serializers import Serializer
from .serializers import RandomSerializer
from rest_framework import viewsets
from .models import RandomData
from django_filters import rest_framework as filters
from url_filter.filtersets import ModelFilterSet
from url_filter.integrations.drf import DjangoFilterBackend
class RandomDataFilterSet(ModelFilterSet):
    class Meta(object):
        model = RandomData
        fields = "__all__"

class RandomDataView(viewsets.ModelViewSet):
    queryset = RandomData.objects.all()
    serializer_class = RandomSerializer
    filter_backends = (DjangoFilterBackend,)

    filter_class = RandomDataFilterSet

    def list(self, request, *args, **kwargs):
        print("called url")
        from .tasks import add
        add.delay()
        return super().list(request, *args, **kwargs)