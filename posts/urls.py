from django.urls import path
from django.views.generic import TemplateView
from .views import PostUpdateDeleteView, CreateReadPostView, CommentView, PostLikeDislikeView,CommentUpdateDeleteView

urlpatterns = [path('get-post/<str:id>/', PostUpdateDeleteView.as_view(), name="get-up-del-post"),
               path('posts/', CreateReadPostView.as_view(), name="create-read-post"),
               path('comments/<str:id>/', CommentView.as_view(), name="comments-on-post"),
               path('like/<str:id>/', PostLikeDislikeView.as_view(), name="like"),
               path('get-comment/<str:id>/', CommentUpdateDeleteView.as_view(), name="comment"),

               ]
