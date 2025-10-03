from rest_framework import serializers
from .models import Post,Category,Tag,Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','slug','description','created_at']
        
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name','slug']
        
        
class CommentSerializer(serializers.ModelSerializer):
    author  = UserSerializer(read_only = True)
    
    class Meta:
        model = Comment
        fields = ['id','post','author','content','created_at','updated_at','is_approved']
        read_only = ['author','created_at','updated_at']
        
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)
    category = CategorySerializer(read_only = True)
    tags = serializers.SerializerMethodField()
    comments  = serializers.SerializerMethodField(read_only = True)
    
    def get_tags(self, obj):
        tags = obj.tags.all()
        return TagSerializer(tags, many=True).data

    def get_comments(self, obj):
        return CommentSerializer(obj.comments.all(), many=True).data
    
    
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source = 'category',
        write_only = True
    )
    
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset = Tag.objects.all(),
        many = True,
        source = 'tag',
        write_only = True
    )
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'author', 'content', 'created_at', 
            'updated_at', 'status', 'category', 'tags', 'comments',
            'category_id', 'tag_ids'
        ]
        read_only_fields = ['author', 'slug', 'created_at', 'updated_at']
        
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'category', 'tags']
    
    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)
        post.tags.set(tags)
        return post