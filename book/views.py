from book.models import Book
from book.serializer import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAll(request):
    title = request.query_params.get('title', None)
    author = request.query_params.get('author', None)
    genre = request.query_params.get('genre', None)

    books = Book.objects.all()
    if title:
        books = books.filter(title__icontains=title)
    if author:
        books = books.filter(author__icontains=author)
    if genre:
        books = books.filter(author__icontains=genre)

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getByID(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response({"error": "book not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)