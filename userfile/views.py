from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.response import Response 
# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
import csv
from rest_framework.parsers import MultiPartParser

def home(request):
    return HttpResponse('Hello')

def index(request):
    return HttpResponse('Thank You')


class UserLoginApiview(APIView):
    permission_classes =[]
    def get_queryset(self):
        queryset = UserLogin.objects.all()
        return queryset
    
    def get(self,request,*agrs,**kwargs):
        users= self,request.user.username
        print('*****',users)
        user_detail = self.get_queryset()
        serializer = UserLoginSerializer(user_detail,many=True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            password = request.data.get('password')
            user.set_password(password)
            user.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserCsvAddApiview(APIView):
    def get_queryset(self):
        queryset = UserCsvFile.objects.all()
        return queryset
    
    # def get(self,request,*args,**kwargs):
    #     users = self.request.user
    #     csv_data=self.get_queryset()
    #     print('*****',users)
    #     serializer = UserCsvAddApiviewSerializer(csv_data,many=True)
    #     return Response(serializer.data)

    def get(self,request,*args,**kwargs):

        users = self.request.user
        if users.is_superuser:
            csv_data=UserCsvFile.objects.all()
            print('*****',csv_data)
            serializer = UserCsvAddApiviewSerializer(csv_data,many=True)
            return Response(serializer.data)
        else:
            try:
                csv_data=UserCsvFile.objects.filter(name__username=users)
                print('*****',csv_data)
                serializer = UserCsvAddApiviewSerializer(csv_data,many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def post(self,request,*args,**kwargs):
        serializer = UserCsvAddApiviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CSVUploadAPIView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        csv_file = request.data['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        csv_reader = csv.DictReader(decoded_file.splitlines())
        for row in csv_reader:
            serializer = CSVSerializer(data=row)
            if serializer.is_valid():
                serializer.save()
            else:
                # Handle validation errors if needed
                pass
        return Response({'message': 'CSV data uploaded successfully'})
    


