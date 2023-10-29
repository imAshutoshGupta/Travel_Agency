from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('booknow', views.book_now),
    path('bookings', views.bookings),
    path('editjourney/<eid>', views.edit_journey),
    path('deletejourney/<did>', views.delete_journey),
]