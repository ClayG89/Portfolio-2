from rest_framework import serializers
from .models import Blog, Comment, Contact

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'blog', 'body')

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(
        many=False,
        read_only=False, 
        queryset=Blog.object.all(),
    )
    class Meta:
        model = Blog
        fields = ('id', 'title', 'blog')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'firstname', 'lastname', 'company', 'phone', 'email', 'topic', 'message')


