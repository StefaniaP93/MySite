from django.urls import path

from . import views


urlpatterns = [
    path('projects/', views.ProjectView.as_view(), name= 'projects_list'),
    path('projects/<slug:project_slug>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('projects-carousel/', views.ImageCarouselView.as_view(), name='project_image'),
]