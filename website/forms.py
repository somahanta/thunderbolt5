from django import forms

# our new form
class ContactForm(forms.Form):
    Name = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )