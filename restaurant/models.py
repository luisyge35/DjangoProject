from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, default = "")
    bookingTime = models.DateField()
    guests = models.SmallIntegerField(default=2)

    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=6, decimal_places=2) 
   inventory = models.SmallIntegerField() 

   def __str__(self):
      return f'{self.title} : {str(self.price)}'
   def get_item(self):
      return f'{self.title} : {str(self.price)}' 