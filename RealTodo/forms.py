from django import forms
from .models import Data , HotelBooking

class TodoForm(forms.ModelForm):
	class Meta:
		model = Data
		fields= ["title", "text"]


class Hotelbooking_form(forms.ModelForm):
	class Meta:
		model  = HotelBooking
		fields = ['name' ,'booking_details','booked_by']