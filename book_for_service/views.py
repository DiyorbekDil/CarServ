from django.shortcuts import render

# Create your views here.


def home_page_view(request, *args, **kwargs):
    return render(request, 'index.html')


def about_page_view(request, *args, **kwargs):
    return render(request, 'about.html')


def booking_page_view(request, *args, **kwargs):
    return render(request, 'booking.html')


def contact_page_view(request, *args, **kwargs):
    return render(request, 'contact.html')


def service_page_view(request, *args, **kwargs):
    return render(request, 'service.html')


def team_page_view(request, *args, **kwargs):
    return render(request, 'team.html')


def testimonial_page_view(request, *args, **kwargs):
    return render(request, 'testimonial.html')


def _404_page_view(request, *args, **kwargs):
    return render(request, '404.html')
