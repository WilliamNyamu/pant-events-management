from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_orgs')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class OrganizationMembership(models.Model):
    ROLES = [
        ('ADMIN', 'Admin'),
        ('EDITOR', 'Editor')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="membership")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name = "organizers")
    joined_at = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=ROLES, default="Editor")

    def __str__(self):
        return f"{self.user} is a {self.role} at {self.organization}"
