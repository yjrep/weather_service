from django import forms


class SearchForm(forms.Form):
    zipcode = forms.RegexField(
        label='',
        required=True,
        min_length=5,
        max_length=5,
        regex='^[0-9]{5}',
        error_messages={
            'invalid': 'Please enter a valid zip code'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Zip Code'
        })
    )
