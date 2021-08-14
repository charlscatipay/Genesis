from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    maker = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.maker}"

class Generation(models.Model):
    generation = models.IntegerField()

    def __str__(self):
        return f"{self.generation}th Gen"

class CoreBrand(models.Model):
    core_brand_name = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.core_brand_name}"


class ProcessorDetail(models.Model):
    thread = models.IntegerField()
    cores = models.IntegerField()
    tdp = models.IntegerField()
    freq = models.DecimalField(max_digits=5, decimal_places=2)
    socket = models.CharField(max_length=10)
    generation = models.ForeignKey(Generation,on_delete=models.DO_NOTHING)
    core_brand = models.ForeignKey(CoreBrand, on_delete=models.DO_NOTHING)
    model_name = models.CharField(max_length=20)
    external_link = models.CharField(max_length=150, blank=True, null=True)
    proc_image = models.ImageField(upload_to='images/processors', null=True, blank=True, verbose_name='Image')

    def __str__(self):
        return f"ID: {self.id} Model Name: {self.model_name}"


class Product(models.Model):
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    manufacture = models.ForeignKey(Manufacturer,on_delete=models.DO_NOTHING)
    processor_detail = models.ForeignKey(ProcessorDetail,on_delete=models.DO_NOTHING, default='')

    def __str__(self):
        return f"ID: {self.id} Model Name : {self.processor_detail.model_name} Price : {self.price} Manufacturer : {self.manufacture}"

