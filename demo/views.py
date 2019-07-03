from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileSerializer
from django.views.decorators.csrf import csrf_exempt
from functools import wraps
from rest_framework.parsers import FileUploadParser
import csv
from django.contrib.auth.models import User
# Create your views here.

def my_decorator(func):
    def wrapper(*args,**kwargs):
        print(args)
        print("Before executing get method")
        print(args[1].user)
        return func(*args,**kwargs)
        print("After executing get method")
    return wraps(func)(wrapper)

class DemoApiView(APIView):
    serializer_class = FileSerializer
    parser_class = (FileUploadParser,)

    @my_decorator
    def get(self,request):
        return Response({
            'data':{
                'message': 'success'
            }
        })

    def post(self,request,*args,**kwargs):
        try:
            serializer = FileSerializer(data=request.data)
            if serializer.is_valid():
                file = serializer.validated_data.get('file')
                print(file.temporary_file_path())
                print(file.content_type)
                with open(file.temporary_file_path(),'r+') as f:
                    readed_message = csv.reader(f)
                    for message in readed_message:
                        print(message)
                return Response({'data': "success" })
            else:
                return Response(serializer.errors)
        except Exception as e:
            print(str(e))
            return Response({'data': str(e)})
