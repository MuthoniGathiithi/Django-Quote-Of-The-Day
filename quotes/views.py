from django.shortcuts import render
from quotes.models import Quote
def random_quote(request):
    quote = Quote.objects.order_by('?').first()  # Get a random quote
    return render(request, 'quotes/quote.html', {'quote': quote})