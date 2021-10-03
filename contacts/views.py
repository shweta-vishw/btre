from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        phone = request.POST['phone']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id, listing_id=listing_id)
            if has_contacted:
                messages.error(request, "You already submitted your query for this listing")
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        send_mail('Property Listing Inquiry', 'There has been an enquiry for ' + listing + ' from '+ name +'.Sign into admin panel for more info', 
        'vishwa@gmail.com', [realtor_email, 'sv10696@gmail.com'], fail_silently=False)
        messages.success(request, "Your request has been submitted, a realtor will be back to you soon")
        return redirect('/listings/'+listing_id)

