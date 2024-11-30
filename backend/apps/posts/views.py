from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .serializer import (
    PostSerializer,
)

from .models import (
    Post,
)

class ListPosts(APIView):

    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetPost(APIView):

    def get(self,request,slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class CreatePost(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):

        if request.method == "POST":
            
            data = {

                'titulo': request.data.get('titulo'),
                'descripcion': request.data.get('descripcion'),
                'imagen': request.data.get('imagen'),
                'user': request.data.get('user')

            }

            serializer = PostSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class EditPost(APIView):

    permission_classes = [IsAuthenticated]

    def put(self,slug,request,*args,**kwargs):
        post = get_object_or_404(Post,slug=slug)

        serializer = PostSerializer(post,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DeletePost(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self,slug,request,*args,**kwargs):
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)