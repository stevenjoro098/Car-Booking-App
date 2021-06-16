from django import forms

class BookingDetailsForm(forms.Form):
    tel_no = forms.IntegerField(label="Enter Phone number")