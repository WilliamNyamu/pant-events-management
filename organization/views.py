from django.shortcuts import render
from .serializers import OrganizationSerializer
from rest_framework import generics
from .models import Organization
from rest_framework import permissions
from .permissions import IsCreatedbyOrReadOnly

# Create your views here.

class OrganizationList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.AllowAny]

class OrganizationCreate(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class OrganizationUpdate(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated, IsCreatedbyOrReadOnly]
