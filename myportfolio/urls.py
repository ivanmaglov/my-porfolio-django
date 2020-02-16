from django.contrib import admin
from django.urls import path,include
from django.conf import  settings
from django.conf.urls.static import static
import myprojects.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', myprojects.views.allprojects, name="allprojects"),
    path('', myprojects.views.home, name="home"),
    path('blog/',include('blog.urls')),
    path('projects/<int:projects_id>', myprojects.views.detail, name='detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # < here
    path('api/', include('myprojects.api.urls',namespace='api')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
