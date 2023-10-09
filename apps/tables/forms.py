from django import forms

class AddToOrderForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    price = forms.IntegerField(min_value=1, initial=1)
    product_id = forms.IntegerField(widget=forms.HiddenInput())