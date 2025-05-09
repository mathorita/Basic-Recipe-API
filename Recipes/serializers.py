from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    ingredients_list = serializers.SerializerMethodField()
    description_list = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'description_list', 'ingredients', 'ingredients_list']

    def get_ingredients_list(self, obj):
        return obj.ingredients.splitlines()

    def get_description_list(self, obj):
        return obj.description.splitlines()