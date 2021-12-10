from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Pacemaker APIs",
        default_version='v1',
        description="API Documentation",
        terms_of_service="/usr/dev/null",
        contact=openapi.Contact(email="vi6hal@gmail.com"),
        license=openapi.License(name="No License"),
    ),
    public=False,
    #    permission_classes=(permissions.AllowAny,),
)

swaggerd = [
    path('apispec', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [
    path('', include("registery.urls")),
    path('manage/', admin.site.urls),
]

urlpatterns = urlpatterns + swaggerd
