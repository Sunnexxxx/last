from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Product, Category
from django.db.models import Q
from .forms import ProductForm, CategoryForm


def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 5)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request, 'products/product_list.html', {'products': products})


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


def category_list(request):
    category_list = Category.objects.all()
    paginator = Paginator(category_list, 5)
    page_number = request.GET.get('page')
    categories = paginator.get_page(page_number)
    return render(request, 'products/category_list.html', {'categories': categories})


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'products/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


class ProductSearchView(ListView):
    model = Product
    template_name = 'products/product_search.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        query = self.get_query()
        if query:
            return Product.objects.filter(Q(name__icontains=query))
        else:
            return Product.objects.none()

    def get_query(self):
        return self.request.GET.get('q', '').strip()


class CategorySearchView(ListView):
    model = Category
    template_name = 'products/category_search.html'
    context_object_name = 'categories'
    paginate_by = 10

    def get_queryset(self):
        query = self.get_query()
        if query:
            return Category.objects.filter(Q(name__icontains=query))
        else:
            return Category.objects.none()

    def get_query(self):
        return self.request.GET.get('q', '').strip()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category_detail.html'
    context_object_name = 'category'
