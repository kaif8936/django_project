from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'author', 'created_date', 'text', 'text_2', 'cover', 'cover_2', 'l_heading', 'l_heading_text', 's_heading', 's_heading_text', 'quote', 'quotes_name', 'tag_1', 'tag_2', 'tag_3',)