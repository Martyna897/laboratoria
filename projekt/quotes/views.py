from django.shortcuts import render, redirect
from .models import Quote
from quotes.migrations.forms import QuoteForm


def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('random_quote')
    else:
        form = QuoteForm()


    return render(request, 'quotes/add_quote.html', {'form': form})


def random_quote(request):
    quote = Quote.objects.order_by('?').first()
    return render(request, 'quotes/random_quote.html', {'quote': quote})