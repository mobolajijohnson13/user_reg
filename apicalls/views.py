import apicalls
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from apicalls.models import Magazine
from apicalls.serializers import MagazineSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def magazine_list(request):
    if request.method == 'GET':
        magazine = Magazine.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            magazine = magazine.filter(title__icontains=title)
        
        magazine_serializer = MagazineSerializer(magazine, many=True)
        return JsonResponse(magazine_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        magazine_data = JSONParser().parse(request)
        magazine_serializer = MagazineSerializer(data=magazine_data)
        if magazine_serializer.is_valid():
            magazine_serializer.save()
            return JsonResponse(magazine_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(magazine_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Magazine.objects.all().delete()
        return JsonResponse({'message': '{} Magazine were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def magazine_detail(request, pk):
    try: 
        magazine = Magazine.objects.get(pk=pk) 
    except Magazine.DoesNotExist: 
        return JsonResponse({'message': 'The magazine does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        magazine_serializer = MagazineSerializer(magazine) 
        return JsonResponse(magazine_serializer.data) 
 
    elif request.method == 'PUT': 
        magazine_data = JSONParser().parse(request) 
        magazine_serializer = MagazineSerializer(magazine, data=magazine_data) 
        if magazine_serializer.is_valid(): 
            magazine_serializer.save() 
            return JsonResponse(magazine_serializer.data) 
        return JsonResponse(magazine_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        magazine.delete() 
        return JsonResponse({'message': 'magazine was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def magazine_list_published(request):
    magazine = Magazine.objects.filter(published=True)
        
    if request.method == 'GET': 
        magazine_serializer = MagazineSerializer(magazine, many=True)
        return JsonResponse(magazine_serializer.data, safe=False)


@api_view(['GET'])
def magazine_list_published_date(request):
    magazine = Magazine.objects.filter(published_date=True)
        
    if request.method == 'GET': 
        magazine_serializer = MagazineSerializer(magazine, many=True)
        return JsonResponse(magazine_serializer.data, safe=False)