from django.db import models
from django.utils import timezone

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Technology', 'Technology'),
        ('News', 'News'),
        ('Sports', 'Sports'),
    )
    cover = models.FileField(default='')
    cover_2 = models.FileField(default='')
    author = models.CharField(max_length=2000, default='')
    title = models.CharField(max_length=2000, default='')
    slug = models.SlugField(default='')
    text = models.TextField(default='')
    text_2 = models.TextField(default='')
    l_heading = models.CharField(max_length=2000, default='')
    l_heading_text = models.CharField(max_length=2000, default='')
    quote = models.CharField(max_length=2000, default='')
    quotes_name = models.CharField(max_length=2000, default='')
    s_heading = models.CharField(max_length=2000, default='')
    s_heading_text = models.CharField(max_length=2000, default='')
    category = models.CharField(max_length=2000, choices=CATEGORY_CHOICES, default='')
    created_date = models.DateTimeField(default='')
    
    tag_1 = models.CharField(max_length=2000, default='')
    tag_2 = models.CharField(max_length=2000, default='')
    tag_3 = models.CharField(max_length=2000, default='')
     
    class Meta:
       ordering = ['-created_date']

    def __str__(self):
        return self.title
