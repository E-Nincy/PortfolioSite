from django.test import TestCase
from .models import Project

class ProjectModelTest(TestCase):
    def test_create_project(self):
        project = Project.objects.create(
            title="Test Project",
            description="Just a test",
            link="https://example.com"
        )
        self.assertEqual(str(project), "Test Project")
