from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return HttpResponse("hello world")

def products(request):
    page_obj= products = Product.objects.all()
    product_name = request.GET.get('product_name')
    if product_name != '' and product_name is not None:
        page_obj = products.filter(name__icontains=product_name)
    
    paginator = Paginator(page_obj, 3)
    page_number = request.GET.get('page')
    page_obj= paginator.get_page('page_number')
    context = {
        'page_obj' : page_obj
    }
    return render(request, 'myapp/index.html', context)
#CREATING A CLASS BASED VIEW FOR LISTING ALL PRODUCTS


'''class ProductListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'
    paginate_by = 3'''


'''def producr_detail(request, id):
    product = Product.objects.get(id = id)
    context = {
        'product' : product
    }
    return render(request, 'myapp/detail.html', context)'''
#CREATING A CLASS BASED VIEW FOR DETAIL PAGE OF ALL PRODUCTS
class ProductDeatilView(DetailView):
    model = Product
    template_name= 'myapp/detail.html'
    context_object_name= 'product'



'''@login_required(login_url='login')
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        images = request.FILES['upload']
        seller_name = request.user
        product = Product(name= name, price=price, desc=desc, images=images, seller_name=seller_name)
        product.save()
        return redirect('myapp:products')
    return render(request, 'myapp/addproduct.html')'''
#CREATING A NEW PRODUCT USING CREATE CLASS VIEW

class ProductCreateView(CreateView):
    model = Product
    fields =['name', 'price', 'desc', 'images', 'seller_name']
    
    #template naming convention modelname_form.html

'''@login_required(login_url='login')
def update_product(request, id):
    product= Product.objects.get(id = id)
    form= ProductUpdateForm()
    if request.method == 'POST':
        forms= ProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('myapp:products')
    else:
        forms = ProductUpdateForm(instance=product)
        

    context = {
        'form' : forms,
        'product' : product
    }
    return render(request, 'myapp/updateproduct.html',context)'''
class ProductUpdateView(UpdateView):
    model = Product
    fields =['name', 'price', 'desc', 'images', 'seller_name']
    template_name_suffix = '_update_form'  #naming convention modelname_update_form

'''@login_required(login_url='login')
def product_delete(request, id):
    product= Product.objects.get(id = id)
    if request.method == 'POST':
        product.delete()
        return redirect('myapp:products')
    context = {
        'product' : product
    }
    return render(request, 'myapp/delete.html', context)'''
# class based view to delete a product
class ProductDeleteView(DeleteView):
    model = Product
    success_url= reverse_lazy('myapp:products')
    #template naming convention is modelname_confirm_delete.html


def seller_detail(request, id):
    seller = User.objects.get(id = id)
    context = {
        'seller' : seller
    }
    return render(request, 'users/sellerdetail.html', context)

def seller_listing(request):
    obj = Product.objects.all()
    myproducts = Product.objects.filter(seller_name=request.user)
    context ={
        'myproducts' : myproducts,
        'obj' : obj
    }
    return render(request, 'users/mylisting.html', context)