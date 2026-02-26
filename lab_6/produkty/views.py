from django.http import JsonResponse


def product_list_api(request):

    produkty = [
        {"id": 1, "name": "Laptop", "price": 3500},
        {"id": 2, "name": "Myszka", "price": 150},
        {"id": 3, "name": "Monitor", "price": 1200},
    ]


    category = request.GET.get('category', 'all')
    print(f"Szukana kategoria: {category}")

    return JsonResponse({"category": category, "products": products})