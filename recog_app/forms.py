from django import forms

class IngredientForm(forms.Form):
    name = forms.CharField(
        max_length=30, 
        widget=forms.TextInput(attrs={'placeholder': 'Ingredient Name'})
    )

    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            