"""test_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.store.views import ProductsAPIView, ProductCategoriesAPIView, ProductRetrieveAPIView, CategoryRetrieveAPIView, \
    UserAPIView, UserRetrieveAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="My api",
        default_version='v1',
        description="RESTful app for provide API for mobile @ web-front applications",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/products/', ProductsAPIView.as_view()),
    path('api/v1/categories/', ProductCategoriesAPIView.as_view()),
    path('api/v1/products/<int:pk>/', ProductRetrieveAPIView.as_view()),
    path('api/v1/categories/<int:pk>/', CategoryRetrieveAPIView.as_view()),
    path('api/v1/users/', UserAPIView.as_view()),
    path('api/v1/users/<int:pk>/', UserRetrieveAPIView.as_view())
]
