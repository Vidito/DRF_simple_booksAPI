# Class Based Views

from rest_framework.views import APIView
from .models import Book
from .serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status



class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookCreate(APIView):
    def post(self, request):
        serizalier = BookSerializer(data=request.data)
        if serizalier.is_valid():
            serizalier.save()
            return Response(serizalier.data)
        else:
            return Response(serizalier.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    def get_book_by_pk(self, pk):
        try:
            return Book.objects.get(id=pk)
        except:
            return Response(
                {'error': 'Book not found'
                },
                status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)