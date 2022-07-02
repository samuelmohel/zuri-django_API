from django.shortcuts import render
from django.contrib.auth.models import User
from links.serializers import LinkSerializer
from .models import Link
from rest_framework import generics
# Create your views here.



class PostListApi(generics.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
    
class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
    
class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer
    
    
class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects/filter(active=True)
    serializer_class = LinkSerializer