from rest_framework import generics
from .models import TruckModel, OwnerModel
from .serializer import TruckModelSerializer, OwnerModelSerializer






class PostTruckModelAPI(generics.ListCreateAPIView):
    queryset = TruckModel.objects.all()
    serializer_class = TruckModelSerializer



class CreateOwnerAPI(generics.ListCreateAPIView):
    queryset = OwnerModel.objects.all()
    serializer_class = OwnerModelSerializer






# class ExtraDataAPI(generics.ListAPIView):
#     queryset = TruckModel.objects.all()
#     serializer_class = ExtraPropertiesModel

