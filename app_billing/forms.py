from django.forms import ModelForm
from .models import Items, Purchase, Order, OrderLine
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ItemCreateForm(ModelForm):
    class Meta:
        model = Items
        fields = '__all__'

class PurchaceCreateForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'billnumber',
            'customer_name',
            'phone_number'
        ]

class OrderLineCreateForm(forms.Form):
    bill_number = forms.CharField()
    product_quantity = forms.IntegerField()
    product_name = Purchase.objects.all().values_list('items__item_name')
    result = [(tp[0], tp[0] )for tp in product_name]
    product_name = forms.ChoiceField(choices=result)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','username','password1','password2',]

class LoginForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField()


class SearchForm(forms.Form):
    search = forms.CharField()