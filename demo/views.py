from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileSerializer
from rest_framework.parsers import FileUploadParser
import csv,io
# Create your views here.
class DemoApiView(APIView):
    serializer_class = FileSerializer
    parser_class = (FileUploadParser,)
    def get(self,request,*args,**kwargs):
        return Response({
            'data':{
                'message': 'success'
            }
        })

    def post(self,request,*args,**kwargs):
        try:
            print(request.data)
            file = request.data.get('file')
            print(file.temporary_file_path())
            print(file.content_type)
            with open(file.temporary_file_path(),'r+') as f:
                readed_message = csv.reader(f)
                for message in readed_message:
                    print(message)
            return Response({'data': "success" })
        except Exception as e:
            print('hello')
            print(str(e))
            return Response({'data': "failed" })
