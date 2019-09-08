from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField

class Projects(models.Model):
    title=models.CharField(max_length=260)
    programming_language=models.CharField(max_length=260)
    framework=models.CharField(max_length=260)
    picture=models.ImageField(upload_to='images/', height_field='height',
        width_field='width')
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    description=RichTextUploadingField(blank=True, null=True,max_length=600)
 #   download=models.FileField(upload_to='myprojects/')
    file = models.FileField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')
    link=models.CharField(max_length=500)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title



