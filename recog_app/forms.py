from django import forms

class IngredientForm(forms.Form):
    name = forms.CharField(
        max_length=30, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Ingredient Name', 
            'class': 'form-control'
        })
    )


class ImageForm(forms.Form):
    image = forms.ImageField(
        label='Take Picture',
        widget=forms.ClearableFileInput(attrs={
            'accept':"image/*", 
            'capture':"environment",
            'class': 'form-control',
            'style': "visibility:hidden;",
            'onchange': "form.submit()"
        })
    )
