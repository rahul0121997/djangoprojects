from . import views
from django.urls import path
from .views import BaseView, PostListView, PostDetailView,CategoryDetailView, TagListView, TagDetailView,CategoryView

app_name = 'blog'  # important for namespacing in templates


# urlpatterns = [
#     path('',views.base,name='base'),
#     path('post-list/',views.post_list,name='post_list'),
#     path('post-detail/<slug:slug>/',views.post_detail,name='post_detail'),
#     path('category-list/',views.category,name='category'),
#     path('category-detail/<slug:slug>/',views.category_detail,name='category_detail'),
#     path('tag-list/',views.tag_list,name='tag_list'),
#     path('tag-detail/<slug:slug>',views.tag_detail,name='tag_detail'),
# ]



urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),  # this is your homepage
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('categories/', CategoryView.as_view(), name='category_list'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tag/<slug:slug>/', TagDetailView.as_view(), name='tag_detail'),
]




