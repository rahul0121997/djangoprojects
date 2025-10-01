from django.contrib import admin
from .models import Post,Category,Tag,Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_per_page = 20
    
@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','description','created_at']
    list_filter = ['name','created_at']
    search_fields = ['name','created_at']
    prepopulated_fields = {'slug': ('name',)} 
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)} 
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','content','created_at','updated_at','is_approved']
    list_filter  = ['author','created_at','updated_at']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']