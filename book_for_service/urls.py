from django.urls import path
from book_for_service.views import *
from book_for_service.views import _404_page_view

urlpatterns = [
    path('about/', about_page_view),
    path('booking/', booking_page_view),
    path('contact/', contact_page_view),
    path('service/', service_page_view),
    path('team/', team_page_view),
    path('testimonial/', testimonial_page_view),
    path('404/', _404_page_view),
    path('', home_page_view),
]