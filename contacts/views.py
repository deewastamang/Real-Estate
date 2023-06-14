from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        realtor_phone = request.POST['realtor_phone']

        # Check Already make an inquery
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You Already Made an inquery for this Property")
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # send mail
        send_mail(
            'Property Listing Inquery',
            'There has been an Inquery for ' + listing + ' .Sign into the Realstate for more',
            'rmsantosh.np@gmail.com',
            [realtor_email, 'pysantosh.np@gmail.com'],
            fail_silently=False,


        )

        messages.success(request, "Your Request has been submitted")
        return redirect('/listings/' + listing_id)


def contact_delete(request, id):
    query = get_object_or_404(Contact, id=id)
    query.delete()
    messages.success(request, "Porperty Deleted")
    return redirect('dashboard')
