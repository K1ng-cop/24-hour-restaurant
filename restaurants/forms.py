from django import forms

class RestaurantFilterForm(forms.Form):
    cuisine_type = forms.CharField(max_length=50, required=False)
    min_rating = forms.FloatField(required=False, min_value=0, max_value=5)
