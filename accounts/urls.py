from rest_framework import routers
from .views import RandomDataView
urlpatterns = []

random = routers.DefaultRouter()
random.register("data",RandomDataView)

urlpatterns += random.urls