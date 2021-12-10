from django.shortcuts import render
from rest_framework import viewsets,mixins
from .models import AppRegistery
from .serializers import AppRegisterySerializer
# Create your views here.
def detail_view(request):
    context ={}         
    return render(request, "registery/setup.html", context)

class RegisteryApiview(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = AppRegistery.objects.all()
    serializer_class = AppRegisterySerializer