from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .forms import ProcessortDetailForm, ProductForm

def show_prod(request):
    product = models.Product
    return render(
        request, template_name= 'products.html',
        context= {'product': product.objects.all()}
    )

def prod_update(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    proc_details = product.processor_detail
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        form2 = ProcessortDetailForm(request.POST, request.FILES, instance=proc_details)
        if form.is_valid():
            product = form.save(commit=False)
            proc_details = form2.save(commit=False)
            product.save()
            proc_details.save()
            return redirect('product')
    else:
        form = ProductForm(instance=product)
        form2 = ProcessortDetailForm(instance=proc_details)
        context = {
            'form': form,
            'form2': form2,
            'message': 'Update this product'
        }
    return render(request, template_name='product_update.html', context=context)

def prod_add(request):
    if request.method=="POST":
        form = ProductForm(request.POST, request.FILES)
        form2 = ProcessortDetailForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            proc_detail = form2.save(commit=False)
            proc_detail.save()
            processor_detail_query = models.ProcessorDetail.objects.get(model_name=form2.cleaned_data['model_name'])
            models.Product.objects.create(
                rating = form.cleaned_data['rating'],
                price = form.cleaned_data['price'],
                manufacture = form.cleaned_data['manufacture'],
                processor_detail = processor_detail_query
            )
            return redirect('product')
    else:
        context = {
            'form': ProductForm(),
            'form2': ProcessortDetailForm(),
            'message' : 'Add new product'
        }
    return render(request, template_name='product_update.html', context=context)
      
