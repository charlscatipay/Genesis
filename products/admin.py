from django.contrib import admin
from .models import Manufacturer, Generation, CoreBrand, Product, ProcessorDetail

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Generation)
admin.site.register(CoreBrand)
admin.site.register(Product)
admin.site.register(ProcessorDetail)
