from django.shortcuts import render, redirect
from listings.models import Listing
from django.core.paginator import Paginator
from listings.choices import city_choices, price_choices, bedroom_choices
from realtors.models import Realtor
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:8]
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    page_listing = paginator.get_page(page)
    context = {
        'listings': page_listing,
        'city_choices': city_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'index.html', context)


def about(request):
    realtors = Realtor.objects.all().order_by('-hire_date')
    som = Realtor.objects.all().filter(is_som=True)
    context = {
        'som': som,
        'realtors': realtors
    }
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            'dtamang1324@gmail.com',
            [email, 'dtamang1324@gmail.com'],
            fail_silently=False,


        )
        messages.success(request, "Your Message has been sent to Realstate")
        return redirect('contact')
    return render(request, 'contact.html')
