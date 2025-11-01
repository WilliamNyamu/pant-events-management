from rest_framework import serializers
from .models import Organization, OrganizationMembership

class OrganizationSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Organization
        fields = ['id', 'name', 'description', 'website', 'instagram_url', 'created_at', 'created_by']
        read_only_fields = ['created_by', 'created_at']

    def validate(self, attrs):
        name = attrs.get('name')
        instance = self.instance # Existing org (if update)

        # Creating a new org
        if not instance and Organization.objects.filter(name=name).exists():
            raise serializers.ValidationError("Organization's name entered is already there.")
        
        # Updating an existing organization
        if instance:
            if Organization.objects.filter(name=name).exclude(pk=instance.pk).exists():
                raise serializers.ValidationError("An organization with the name already exists")
        
        return attrs
        