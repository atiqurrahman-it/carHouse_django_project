from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Cars
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def Car(request):
    t_car = Cars.objects.order_by('-create_data')

    model_search = Cars.objects.values_list('model', flat=True).distinct()
    city_search = Cars.objects.values_list('city', flat=True).distinct()
    year_search = Cars.objects.values_list('year', flat=True).distinct()
    body_style_search = Cars.objects.values_list('body_style', flat=True).distinct()

    paginator = Paginator(t_car, 4)  # Show 3 cars per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        "t_car": page_obj,
        "model_search": model_search,
        "city_search": city_search,
        "year_search": year_search,
        "body_style_search": body_style_search,
    }
    return render(request, 'cars/cars.html', data)


def Car_details(request, id):
    single_car_details = get_object_or_404(Cars, id=id)
    data = {
        "car_details": single_car_details
    }
    return render(request, 'cars/car_details.html', data)


def Search(request):
    cars = Cars.objects.order_by('-create_data')

    model_search = Cars.objects.values_list('model', flat=True).distinct()
    city_search = Cars.objects.values_list('city', flat=True).distinct()
    year_search = Cars.objects.values_list('year', flat=True).distinct()
    body_style_search = Cars.objects.values_list('body_style', flat=True).distinct()
    transmissions_search = Cars.objects.values_list('transmission', flat=True).distinct()

    if 'keyword_search' in request.POST:
        keyword = request.POST.get('keyword_search')
        if keyword:
            cars = Cars.objects.filter(description__icontains=keyword)

    if 'search_model' in request.POST:
        model = request.POST.get('search_model')
        if model:
            cars = Cars.objects.filter(model__iexact=model)

    if 'search_city' in request.POST:
        city = request.POST.get('search_city')
        if city:
            cars = Cars.objects.filter(city__iexact=city)

    if 'search_year' in request.POST:
        year = request.POST.get('search_year')
        if year:
            cars = Cars.objects.filter(year__iexact=year)

    if 'search_body_type' in request.POST:
        body_type = request.POST.get('search_body_type')
        if body_type:
            cars = Cars.objects.filter(body_style__iexact=body_type)

    if 'trans_search' in request.POST:
        transmissions = request.POST.get('trans_search')
        if transmissions:
            cars = Cars.objects.filter(transmission__iexact=transmissions)

    if 'min_price' in request.GET:
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        if max_price:
            cars = Cars.objects.filter(price__get=min_price, price__let=max_price)

    data = {
        "cars": cars,

        "model_search": model_search,
        "city_search": city_search,
        "year_search": year_search,
        "body_style_search": body_style_search,
        "transmissions_search": transmissions_search,
    }
    return render(request, 'cars/search.html', data)
