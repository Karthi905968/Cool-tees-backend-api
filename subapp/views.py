from rest_framework import generics
from .serializers import PostSerializer
from .models import PostModel
from django.http import JsonResponse
# Create your views here.

class PostView(generics.ListAPIView):
    queryset = PostModel.objects.order_by('created_at').reverse().all()
    serializer_class = PostSerializer

class PostAdd(generics.CreateAPIView):
     queryset = PostModel.objects.all()
     serializer_class = PostSerializer

class PostUpdate(generics.RetrieveAPIView,generics.UpdateAPIView):
       queryset = PostModel.objects.all()
       serializer_class = PostSerializer

class PostDelete(generics.DestroyAPIView):
      queryset = PostModel.objects.all()
      serializer_class = PostSerializer

def IncrementLike(request,post_id):
      # get the post
      post = PostModel.objects.get(id=post_id)

      #add count
      new_count = post.count + 1
      post.count = new_count

      #save
      post.save()

      return JsonResponse({'result':'Successful'})

def DecrementLike(request,post_id):
      # get the post
      post = PostModel.objects.get(id=post_id)

      #add count
      new_count = post.count - 1
      post.count = new_count

      #save
      post.save()

      return JsonResponse({'result':'Successful'})
      
     
     
