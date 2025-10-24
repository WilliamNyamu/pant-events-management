from rest_framework import serializers
from .models import Organization, OrganizationMembership

class OrganizationSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Organization
        fields = ['id', 'name', 'description', 'website', 'instagram_url', 'created_at', 'created_by']
        read_only_fields = ['created_by', 'created_at']

    def validate(self, attrs):
        name = attrs.get('name')

        if Organization.objects.filter(name = name).exists():
            serializers.ValidationError("Organization's name entered is already there.")
        
        