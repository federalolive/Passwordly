from django import forms

class PasswordGeneratorForm(forms.Form):
  length = forms.IntegerField(min_value=4, max_value=128)
  use_upper = forms.BooleanField(initial=True, required=False)
  use_lower = forms.BooleanField(initial=True, required=False)
  use_digits = forms.BooleanField(initial=True, required=False)
  use_special = forms.BooleanField(initial=True, required=False)
  avoid_similar = forms.BooleanField(initial=True, required=False)