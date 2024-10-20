from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response

from review.models import Review
from review.serializer import ReviewSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user_id=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return (Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getReviewByBookID(request, book_id):
    try:
        reviews = Review.objects.filter(book_id=book_id)
        if not reviews.exists():
            return Response({"msg": "no reviews"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getReviewByUserID(request, user_id):
    try:
        reviews = Review.objects.filter(user_id=user_id)
        if not reviews.exists():
            return Response({"msg": "no reviews"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)