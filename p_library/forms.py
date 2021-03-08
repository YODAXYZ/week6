from django import forms
from p_library.models import Author, UserProfile


class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age']