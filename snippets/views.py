from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from snippets.serializers import SnippetSerializers
from snippets.models import Snippet

class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializers(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =  SnippetSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    def get_obj(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk, format=None):
        snippet = self.get_obj(pk) 
        serializer = SnippetSerializers(snippet)
        return Response(serializas_viewer.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_obj(pk) 
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_obj(pk) 
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)