from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet, ModelViewSet
from blog.serializers import ItemSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from blog.models import Item
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, permissions
from django.contrib.auth.models import User




class UserViewSet(ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

class UserCreate(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
