from django.db import models



# Create your models here.
class ProductsModel(models.Model):
    user = models.ForeignKey('userapp.CustomUserrr',on_delete = models.CASCADE)
    itemname = models.CharField(max_length = 100)
    itemdescription = models.TextField()
    price = models.IntegerField()
    catogry = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
    discount = models.IntegerField(null = True)

    def save(self,*args,**kwargs):
        user =  self.user.is_staff
        if user:
            super().save()
        else:
            return False
        
   