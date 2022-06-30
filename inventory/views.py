from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse

from inventory.models import Inventory

# Create your views here.
class HomeView(TemplateView):
    template_name = 'inventory/home.html'

class InventoryList(ListView):
    paginate_by = 2
    model = Inventory
    template_name =  'inventory/inventory_list.html'
    context_object_name = 'inventories'

class InventoryDetail(DetailView):
    model = Inventory
    context_object_name = 'inventory'

class InventoryAdd(CreateView):
    model = Inventory
    fields = ['product_name', 'sku', 'price']

    def get_success_url(self) -> str:
        return reverse('inventory-list')

class InventoryEdit(UpdateView):
    model = Inventory
    fields = ['product_name', 'sku', 'price']
    action = 'Update'

    def get_success_url(self):
        return reverse(
            "inventory-detail",
            kwargs={'pk':self.kwargs['pk']}
        )