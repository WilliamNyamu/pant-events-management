from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.OrganizationList.as_view(), name='organizations'),
    path('create/', views.OrganizationCreate.as_view(), name='organization-create'),
    path('<int:pk>/update/', views.OrganizationUpdate.as_view(), name='organization-update')
]