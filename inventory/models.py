from django.db import models

# Create your models here.
# ID, SKU, Product Name, Price, Date

class Inventory(models.Model):
    class Meta:
        verbose_name_plural = 'Inventory'
        unique_together = ('sku', 'product_name',)
        ordering = ('-updated_at', ) # Added just now


    sku = models.CharField(max_length=32, blank=False)
    product_name = models.CharField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<id={self.id} name={self.product_name} sku={self.sku}>"
