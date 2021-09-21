from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView, Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from books.serializer import BookSerializer
from books.models import Book


class BooksList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetails(APIView):

    def get_book(self, id: int):
        try:
            return Book.objects.get(id=id)
        except:
            raise Http404

    def get(self, request: Request, id: str):
        book = self.get_book(id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request: Request, id: str):
        book = self.get_book(id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: str):
        book = self.get_book(id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
