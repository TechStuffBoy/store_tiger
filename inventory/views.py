from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages

from inventory.models import Inventory



# Create your views here.
class HomeView(TemplateView):
    template_name = 'inventory/home.html'

class InventoryList(ListView):
    paginate_by = 2
    model = Inventory
    template_name =  'inventory/inventory_list.html'
    context_object_name = 'inventories'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Inventory.objects.filter(
                Q(product_name__icontains=query) |
                Q(sku__icontains=query) |
                Q(date__contains=query) |
                Q(price__contains=query)
            )
        else:
            return Inventory.objects.all()

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

def upload_csv(request):
    if request.method == 'POST':
        print('came here')

        # Process the file
        # print(request.FILES)
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("inventory-list"))
        
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        lines = (line.strip() for line in lines) # changed to generator
        # print(lines)

        # Loop through the list and append to the model
        for line in lines:
            fields = line.split(',')
            print(fields)
            try:
                _ , created = Inventory.objects.update_or_create(
                    product_name=fields[0],
                    sku=fields[1],
                    price=fields[2],
                )
            except IntegrityError as e:
                messages.warning(request, f"{line} already there.. Please correct and try again!")
                return HttpResponseRedirect(reverse("inventory-list"))

        messages.success(request, 'Successfully created/updated all the entries')
            

        # Send the redirect to the inventory-list
        return HttpResponseRedirect(reverse("inventory-list"))
        