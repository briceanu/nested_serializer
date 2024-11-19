from rest_framework import serializers
from .models import TruckModel, Colors,Fuel_type, TruckBrands
from .models import OwnerModel




class TruckModelSerializer(serializers.ModelSerializer):
    fuel_consumption = serializers.SerializerMethodField()

    class Meta:
        model = TruckModel
        fields = '__all__'


    def validate_brand(self,value):
        if value not in TruckBrands.values:
            valid_trucks = ', '.join(TruckBrands.values)
            raise serializers.ValidationError(f'Allowed trucks are {valid_trucks}')
        return value




    def validate_color(self, value):
        if value not in Colors.values:
            allowed_color = ', '.join(Colors.values)
            raise serializers.ValidationError(f"Valid colors are: {allowed_color}")
        return value

    def validate_fuel_type(self, value):
        if value not in Fuel_type.values:
            allowed_fuel_type = ', '.join(Fuel_type.values)
            raise serializers.ValidationError(f"Valid fuel is: {allowed_fuel_type}")
        return value


    def get_fuel_consumption(self,obj):
        return round( obj.fuel_consumption,2 )
    

class OwnerModelSerializer(serializers.ModelSerializer):
    truck = TruckModelSerializer(read_only=True)
    class Meta:
        model = OwnerModel
        fields =['owner_id','age','email','address','truck']

     
    


