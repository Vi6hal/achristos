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
    # filter_fields = ['id', 'first_name','last_name','address']
    filter_class = RandomDataFilterSet

    # def list(self, request, *args, **kwargs):
    #     fake_ins = faker.Faker()
    #     for i in range(1,100):
    #         RandomData.objects.create(
    #             **{'address':fake_ins.address(),
    #             'first_name':fake_ins.first_name(),
    #             'last_name':fake_ins.last_name()
    #             }
    #         )
    #     return super().list(request, *args, **kwargs)
