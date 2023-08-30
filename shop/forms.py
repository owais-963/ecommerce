from django import forms
from .models import Customer, Address


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # confirm_password = forms.CharField(widget=forms.PasswordInput)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Date of Birth')

    class Meta:
        model = Customer
        fields = ['Fname', 'Lname', 'email', 'password', 'NICno', 'phoneNo', 'dob']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['country', 'state', 'city', 'postal_code', 'street_add']
