from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    hook_text = models.CharField(max_length=100, blank=True)
    content = RichTextField()
    
    head_image = models.ImageField(upload_to='blogs/images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    reference = models.CharField(max_length=100, blank=True)
    
    # admin에서 작성자가 쓴 title 형태로 보기
    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    