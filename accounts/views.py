from rest_framework.serializers import Serializer
from .serializers import RandomSerializer
from rest_framework import viewsets
from .models import RandomData
import faker
class RandomDataView(viewsets.ModelViewSet):
    queryset = RandomData.objects.all()
    serializer_class = RandomSerializer
    def list(self, request, *args, **kwargs):
        fake_ins = faker.Faker()
        for i in range(1,100):
            RandomData.objects.create(
                **{'address':fake_ins.address(),
                'first_name':fake_ins.first_name(),
                'last_name':fake_ins.last_name()
                }
            )
        return super().list(request, *args, **kwargs)
