from django.urls import path
from .views import PostView,PostAdd,PostUpdate,PostDelete,IncrementLike,DecrementLike
urlpatterns = [
    path('',PostView.as_view(),name='post'),
    path('add/',PostAdd.as_view(),name='post-add'),
    path('update/<int:pk>/',PostUpdate.as_view(),name='post-update'),
    path('delete/<int:pk>/',PostDelete.as_view(),name='post-delete'),
    path('like/add/<int:post_id>/',IncrementLike,name='like-add'),
    path('like/substract/<int:post_id>/',DecrementLike,name='like-substract'),
    
]