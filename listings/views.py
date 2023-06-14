from django.shortcuts import render, get_object_or_404
from .models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator
from .choices import bedroom_choices, price_choices, city_choices

from .utils import render_to_pdf
from django.views.generic import View
from django.template.loader import get_template
from django.http import HttpResponse
# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    page_listing = paginator.get_page(page)
    context = {
        'listings': page_listing,
        'city_choices': city_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'listings/listings.html', context)


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/list_detail.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    # Prices
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list,
        'city_choices': city_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)


class GeneratePDF(View):
    def get(self, request, listing_id, *args, **kwargs):
        listing = get_object_or_404(Listing, pk=listing_id)
        template = get_template('listings/pdf.html')
        context = {
            'listing': listing
        }
        html = template.render(context)
        pdf = render_to_pdf('listings/pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % (listing_id)
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
