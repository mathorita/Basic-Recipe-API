from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Recipe
from .serializers import RecipeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend]
    
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    filterset_fields = {
        'title': ['icontains'],
        'ingredients': ['icontains'],
    }