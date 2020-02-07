from rest_framework import serializers
from ..models import Projects

class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Projects
        fields=['title','programming_language','framework','picture','description','file','link','pub_date']
