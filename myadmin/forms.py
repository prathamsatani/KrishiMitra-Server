from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                "placeholder": "Username",
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                "placeholder": "Password",
            }
        )


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500",
                "placeholder": "Email",
            }
        ),
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500",
                "placeholder": "First Name",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500",
                "placeholder": "Last Name",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "is_staff",
            "is_superuser",
        )

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "w-full px-4 py-2 rounded-lg bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500",
                "placeholder": "Username",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "class": "w-full px-4 py-2 rounded-lg bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500",
                "placeholder": "Password",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "class": "w-full px-4 py-2 rounded-lg bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500",
                "placeholder": "Confirm Password",
            }
        )
        self.fields["is_staff"].widget.attrs.update(
            {
                "class": "w-full px-4 py-2 rounded-lg h-6 w-6 bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500",
            }
        )
        self.fields["is_superuser"].widget.attrs.update(
            {
                "class": "w-full px-4 py-2 rounded-lg h-6 w-6 bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500",
            }
        )
    
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.is_staff = self.cleaned_data["is_staff"]
        user.is_superuser = self.cleaned_data["is_superuser"]
        
        if commit:
            user.save()
        return user