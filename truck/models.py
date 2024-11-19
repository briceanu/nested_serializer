from django.db import models
import uuid



class Colors(models.TextChoices):
    BLUE = 'blue'
    RED = 'red'
    BLACK = 'black'

class Fuel_type(models.TextChoices):
    DIESEL = 'diesel'
    LPG  = 'lpg_gas'



class TruckBrands(models.TextChoices):
    SCANIA = 'Scania',
    MERCEDES = 'Mercedes',
    DAF = 'Daf'


# create a truck model 

# create a ownerModel

class TruckModel(models.Model):
    truck_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    brand = models.CharField(max_length=20,null=False)
    weight  = models.DecimalField(max_digits=5,decimal_places=2,blank=False)
    fuel_consumption_per_day = models.DecimalField(max_digits=4,decimal_places=2)
    distance = models.FloatField(max_length=5, blank=False)
    color = models.CharField(max_length=10,null=False)
    fuel_type = models.CharField(max_length=10,null=False)

    @property
    def fuel_consumption(self):
        return  (float(self.fuel_consumption_per_day ) / self.distance) * 100






class OwnerModel(models.Model):
    
    owner_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    age = models.SmallIntegerField( null=False)
    email = models.EmailField(null=False,max_length=30)
    address = models.CharField(max_length=100,null=False)
    truck = models.OneToOneField(TruckModel,on_delete=models.CASCADE, related_name='truck')




