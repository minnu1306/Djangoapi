from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSe
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

class ModelView(viewsets.ModelViewSet):
    serializer_class=ArticleSe
    queryset=Article.objects.all()

class ArticleView(viewsets.ViewSet):
    def list(self,request):
        article=Article.objects.all()
        serializer= ArticleSe(article, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer=ArticleSe(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        article=Article.objects.get(pk=pk)
        serializer= ArticleSe(article)
        return Response(serializer.data)

    def update(self,request,pk=None):
        article=Article.objects.get(pk=pk)
        serializer=ArticleSe(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class GenericV(generics.GenericAPIView,mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
     serializer_class=ArticleSe
     queryset=Article.objects.all()
     lookup_field='id'
     def get(self,request,id=None):
         if id:
             return self.retrieve(request)
         else:
             return self.list(request)


     def post(self,request,id=None):
         return self.create(request)

     def put(self,request, id=None):
         return self.update(request,id)

     def delete(self,request,id=None):
         return self.destroy(request,id)


class ArticleList(APIView):
    def get(self,request):
        if request.method=='GET':
            article=Article.objects.all()
            serializer= ArticleSe(article, many=True)
            return Response(serializer.data)

    def post(self,request):
        serializer=ArticleSe(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def article_list(request):
    if request.method=='GET':
        article=Article.objects.all()
        serializer= ArticleSe(article, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        #data=JSONParser().parse(request)
        serializer=ArticleSe(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Create your views here.
