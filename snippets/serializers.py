from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={"base_template": "textarea.html"})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     owner = serializers.ReadOnlyField(source="owner.username")

#     def create(self, validated_data): 
#         return Snippet.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.validated_data)
#         instance.code = validated_data.get("code", instance.validated_data)
#         instance.linenos = validated_data.get("linenos", instance.validated_data)
#         instance.language = validated_data.get("language", instance.validated_data)
#         instance.style = validated_data.get("style", instance.validated_data)

#         instance.save()
#         return instance

## This is an easier way to do what i did manually above but it gives less control

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'created_date', 'title', 'code', 'linenos', 'language', 'style']