from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def home(request,id=None):
    if request.method == 'GET':
        queryset = developer.objects.all()
        serializer_class = dev_serializer(queryset,many=True)
        return Response(serializer_class.data,status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        print(data)
        serializer_class = dev_serializer(data=data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        data = request.data
        print(data)
        instance = developer.objects.get(id=id)
        serializer_class = dev_serializer(instance,data=data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_200_OK)
            
    elif request.method == 'PATCH':
        data = request.data
        print(data)
        instance = developer.objects.get(id=id)
        serializer_class = dev_serializer(instance,data=data,partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        data=request.data
        instance = developer.objects.get(id=id)
        instance.delete()
        return Response({"message":"deleted succesfully."},status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        
          
    