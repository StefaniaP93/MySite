from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectSerializer


class ImageCarouselView(APIView):
    def get(self, request):
        projects = Project.objects.filter(carousel=True)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class ProjectView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
class ProjectDetail(APIView):
    def get_object(self, request, project_slug):
        try:
            return Project.objects.get(slug=project_slug)
        except Project.DoesNotExist:
            raise Http404

        
    def get(self, request, project_slug):
        project = self.get_object(request, project_slug)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK) 

