from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class post(models.Model):
    post_img = models.ImageField(null=True, blank=True)
    post_title = models.CharField(max_length=600)
    post_text = RichTextField(null=True, blank=True)
    author = models.ForeignKey('auth.User',name='author',  on_delete=models.CASCADE)

    post_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.post_title

    
    def get_absolute_url(self):
        return reverse('postView', args=[str(self.pk)])