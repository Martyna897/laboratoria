from django.shortcuts import render
from .models import Visit

def home_view(request):
    v, created = Visit.objects.get_or_create(id=1)
    v.count += 1
    v.save()
    return render(request, 'visit_count.html', {
        'visit_count': v.count
    })

def reset_count(request):
    v, created = Visit.objects.get_or_create(id=1)
    v.count = 0
    v.save()
    return render(request, 'visit_count.html', {
        'visit_count': v.count
    })