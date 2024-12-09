from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from app.models import *
from app.serializers import *
from rest_framework.response import Response

@permission_classes([IsAuthenticated])
class Crud(APIView):
    def get(self,request,pk=None):
        if(pk):
            OBJ=Product.objects.get(id=pk)
            Serialized_obj=Product_Serializers(OBJ)
            return Response(Serialized_obj.data)
        else:
            OBJ=Product.objects.all()
            Serialized_obj=Product_Serializers(OBJ,many=True)
            return Response(Serialized_obj.data)
    def post(self,request,pk=None):
        data=Product_Serializers(data=request.data)
        if data.is_valid():
            data.save()
            return Response({'Done':'Successsfull'})
    def put(self,request,pk=None):
        OBJ=Product.objects.get(id=pk)
        Update_Obj=Product_Serializers(OBJ,data=request.data)
        if Update_Obj.is_valid():
            Update_Obj.save()
            return Response({'Done':'Update Successsfull'})
    
    def patch(self,request,pk=None):
        OBJ=Product.objects.get(id=pk)
        Update_Obj=Product_Serializers(OBJ,data=request.data,partial=True)
        if Update_Obj.is_valid():
            Update_Obj.save()
            return Response({'Done':'Update Successsfull'})
    def delete(self,request,pk=None):
        Obj=Product.objects.get(id=pk).delete()
        return Response({'Done':'Delete Successsfull'})


    