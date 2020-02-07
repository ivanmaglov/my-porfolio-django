from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('projects', views.ProjectsViewSet)


app_name='myprojects'

urlpatterns= [
    path('', include(router.urls)),
    path('myprojects', views.ProjectsListView.as_view(), name='projects_list'),
    path('myprojects/<pk>/', views.ProjectsDetailView.as_view(), name='projects_detail'),
]