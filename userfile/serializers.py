from rest_framework import serializers
from .models import *
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ['id','username','password']

class UserCsvAddApiviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCsvFile
        fields = ['id','name','csv_file']


class CSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVModel
        fields = '__all__'