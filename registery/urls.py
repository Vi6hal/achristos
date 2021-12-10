from django.urls import path
from .views import detail_view,RegisteryApiview
from rest_framework import routers
apiroute = routers.DefaultRouter()
apiroute.register("brew",RegisteryApiview)
urlpatterns = [
    path('', detail_view),
]
urlpatterns +=apiroute.urls