from django.db import models


class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category} - ₹{self.amount}"
