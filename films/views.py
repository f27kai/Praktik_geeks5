from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import FilmSerializer
from .models import Movie


@api_view(['GET'])
def movies_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response({"error_message": "Moview not found"},status=status.HTTP_404_NOT_FOUND)
    data = FilmSerializer(movie).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def movies_list_api_view(request):
    movies = Movie.objects.all()
    data = FilmSerializer(movies, many=True).data





    # data = {
    #     'text': "Hello World"
    # }
    # list = [
    #     'hello', 'world', '!'
    # ]
    return Response(data=data, status=status.HTTP_200_OK)
