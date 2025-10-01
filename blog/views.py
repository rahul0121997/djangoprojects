# from django.shortcuts import render,get_object_or_404,redirect
# from .models import Category,Tag,Post,Comment
# from django.contrib import messages

# def base(request):
#     return render(request,'blog/base.html')

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html',{'posts':posts})

# def post_detail(request, slug):
#     """
#     Display single post with comments
#     Handle comment submission
#     """
#     post = get_object_or_404(Post, slug=slug, status='published')
#     comments = Post.comments.filter(active=True).select_related('author')
    
#     # Handle comment submission
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             content = request.POST.get('content')
#             if content:
#                 Comment.objects.create(
#                     post=post,
#                     author=request.user,
#                     content=content,
#                     active=True
#                 )
#                 messages.success(request, 'Your comment has been posted!')
#                 return redirect('blog:post_detail', slug=slug)
#         else:
#             messages.error(request, 'You must be logged in to comment.')
    
#     context = {
#         'post': post,
#         'comments': comments,
#     }
#     return render(request, 'blog/post_detail.html', context)

# def category(request):
#     categories = Category.objects.all()
#     return render(request,'blog/category.html',{'categories':categories})

# def category_detail(request, slug):
#     """
#     Display all posts in a specific category
#     """
#     category = get_object_or_404(Category, slug=slug)
#     posts = category.posts.filter(status='published').select_related('author').prefetch_related('tags')
    
#     context = {
#         'category': category,
#         'posts': posts,
#     }
#     return render(request, 'blog/category_detail.html', context)

# def tag_list(request):
#     tags = Tag.objects.all()
#     return render(request,'blog/tag_list.html',{'tags':tags})


# def tag_detail(request, slug):
#     """
#     Display all posts with a specific tag
#     """
#     tag = get_object_or_404(Tag, slug=slug)
#     posts = tag.posts.filter(status='published').select_related('author', 'category').prefetch_related('tags')
    
#     context = {
#         'tag': tag,
#         'posts': posts,
#     }
#     return render(request, 'blog/tag_detail.html', context)




from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Category, Tag, Post, Comment
from django.views.generic import DetailView


# -----------------------
# Base Page
# -----------------------
class BaseView(View):
    def get(self, request):
        return render(request, 'blog/base.html')


# -----------------------
# Post List
# -----------------------
class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/post_list.html', {'posts': posts})


# -----------------------
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context['comments'] = post.comments.filter().select_related('author')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        post = self.object

        if request.user.is_authenticated:
            content = request.POST.get('content')
            if content:
                Comment.objects.create(
                    post=post,
                    author=request.user,
                    content=content
                )
                messages.success(request, 'Your comment has been posted!')
                return redirect('blog:post_detail', slug=post.slug)
        else:
            messages.error(request, 'You must be logged in to comment.')

        context = self.get_context_data()
        return self.render_to_response(context)


# -----------------------
# Category List
# -----------------------
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'blog/category.html', {'categories': categories})


# -----------------------
# Category Detail
# -----------------------
# class CategoryDetailView(View):
#     def get(self, request, slug):
#         category = get_object_or_404(Category, slug=slug)
#         # posts = category.posts.filter(status='published').select_related('author').prefetch_related('tags')  # ← lowercase 'c'
#         posts = category.posts.filter(status = 'published')
#         context = {
#             'category': category,
#             'posts': posts,
#         }
#         return render(request, 'blog/category_detail.html', context)


# -----------------------
# Tag List
# -----------------------
class TagListView(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'blog/tag_list.html', {'tags': tags})


# -----------------------
# Tag Detail
# -----------------------
# class TagDetailView(View):
#     def get(self, request, slug):
#         tag = get_object_or_404(Tag, slug=slug)
#         posts = tag.posts.filter(status='published').select_related('author', 'category').prefetch_related('tags')

#         context = {
#             'tag': tag,
#             'posts': posts,
#         }
#         return render(request, 'blog/tag_detail.html', context)


# blog/views.py

class CategoryDetailView(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        # Remove the status filter if Post model doesn't have status field
        posts = category.posts.all().select_related('author').prefetch_related('tags')

        context = {
            'category': category,
            'posts': posts,
        }
        return render(request, 'blog/category_detail.html', context)

class TagDetailView(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        # Remove the status filter if Post model doesn't have status field
        posts = tag.posts.all().select_related('author', 'category').prefetch_related('tags')

        context = {
            'tag': tag,
            'posts': posts,
        }
        return render(request, 'blog/tag_detail.html', context)