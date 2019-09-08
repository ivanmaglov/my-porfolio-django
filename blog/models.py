from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField

class Blog(models.Model):
    title=models.CharField(max_length=260)
    p_date=models.DateTimeField()
    post=RichTextUploadingField(blank=True, null=True)
    image=models.ImageField(upload_to='images/', null=True,blank=True)
 #   file=models.FileField(upload_to='projects/')

    def __str__(self):
        return self.title

    def pub_date_petty(self):
        return self.p_date.strftime('%b %e %Y')

    def summary(self):
        return self.post[:290]
