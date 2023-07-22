from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from quotations.models import Quotation
from appstore.models import Customer

def quotations(request):
    quotations = Quotation.objects.all().values()
    template = loader.get_template('quotation.html')
    context = {
       'quotations': quotations,
    }
    return HttpResponse(template.render(context, request))
def customers(request):
  mycustomers = Customer.objects.all().values()
  template = loader.get_template('all_customers.html')
  context = {
    'mycustomers': mycustomers,
  }
  return HttpResponse(template.render(context, request))
def my_view(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id)

    context = {
        'customer': customer,
    }
    return render(request, 'your_template.html', context)
