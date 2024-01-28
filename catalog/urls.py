from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ProductUpdateView, ContactsView, ProductCreateView, \
    ProductDeleteView, CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDetailView, CategoryDeleteView, \
    toggle_activity
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='list_product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('edit_product/<int:pk>', ProductUpdateView.as_view(), name='edit_product'),
    path('view_product/<int:pk>', ProductDetailView.as_view(), name='view_product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('list_category/', CategoryListView.as_view(), name='list_category'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('edit_category/<int:pk>', CategoryUpdateView.as_view(), name='edit_category'),
    path('view_category/<int:pk>', CategoryDetailView.as_view(), name='view_category'),
    path('delete_category/<int:pk>', CategoryDeleteView.as_view(), name='delete_category'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('activity/<int:pk>', toggle_activity, name='toggle_activity'),
]
