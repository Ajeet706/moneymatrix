from django.shortcuts import render
from .models import Expense
from django.db.models import Sum

def home(request):
    expenses = Expense.objects.all().order_by('-date')
    total = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'home.html', {'expenses': expenses, 'total': total})
