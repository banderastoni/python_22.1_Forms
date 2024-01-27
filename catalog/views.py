from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView, DeleteView

from catalog.models import Product, Category


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Продукт',
    }


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category')  # Поля для редактирования
    success_url = reverse_lazy('catalog:list_product')  # Адрес для перенаправления после успешного редактирования


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category')
    success_url = reverse_lazy('catalog:list_product')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list_product')


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории',
    }
    template_name = 'catalog/category_list.html'


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name', 'description')
    success_url = reverse_lazy('catalog:list_category')


class CategoryDetailView(DetailView):
    model = Category
    extra_context = {
        'title': 'Категория',
    }
    template_name = 'catalog/category_detail.html'


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name', 'description')
    success_url = reverse_lazy('catalog:list_category')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('catalog:list_category')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты',
    }
