from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

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