from django import forms  
from .models import Author, Book  
  
class AuthorForm(forms.ModelForm):

    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:  
        model = Author  
        fields = '__all__'

class BookForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput)

    class Meta:  
        model = Book  
        fields = '__all__'