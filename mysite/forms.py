from django import forms
from django.forms import TextInput, EmailInput, PasswordInput
from .models import Signup
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class MyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
            # Add margin to the bottom of each field
            field.widget.attrs["class"] = field.widget.attrs.get("class", "") + " mb-4"

    class Meta:
        model = Signup
        fields = "__all__"
        widgets = {
            "email": EmailInput(
                attrs={
                    "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                    "placeholder": "Email",
                }
            ),
            "username": TextInput(
                attrs={
                    "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                    "placeholder": "Username",
                }
            ),
            "first_name": TextInput(
                attrs={
                    "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                    "placeholder": "First Name",
                }
            ),
            "last_name": TextInput(
                attrs={
                    "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                    "placeholder": "Last Name",
                }
            ),
            "password": PasswordInput(
                attrs={
                    "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                    "placeholder": "Password",
                }
            ),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500",
                "placeholder": "Username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500",
                "placeholder": "Password",
            }
        )
    )


class FertilizerRecommenderForm(forms.Form):
    CROP_CHOICES = [
        ("", "Select the type of crop you'd like to grow"),
        (0, "Sugarcane"),
        (1, "Jowar"),
        (2, "Cotton"),
        (3, "Rice"),
        (4, "Wheat"),
        (5, "Groundnut"),
        (6, "Maize"),
        (7, "Tur"),
        (8, "Urad"),
        (9, "Moong"),
        (10, "Gram"),
        (11, "Masoor"),
        (12, "Soybean"),
        (13, "Ginger"),
        (14, "Turmeric"),
        (15, "Grapes"),
    ]

    SOIL_CHOICES = [
        ("", "Select the type of soil you want to grow on"),
        (0, "Black"),
        (1, "Red "),
        (2, "Medium Brown"),
        (3, "Dark Brown"),
        (4, "Red"),
        (5, "Light Brown"),
        (6, "Reddish Brown"),
    ]

    crop = forms.ChoiceField(
        choices=CROP_CHOICES,
        widget=forms.Select(
            attrs={"class": "w-full p-2 border border-gray-300 rounded"}
        ),
    )
    soil = forms.ChoiceField(
        choices=SOIL_CHOICES,
        widget=forms.Select(
            attrs={"class": "w-full p-2 border border-gray-300 rounded"}
        ),
    )
    nitrogen = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Nitrogen Content in (kg/ha)",
            }
        )
    )
    phosphorus = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Phosphorus Content in (kg/ha)",
            }
        )
    )
    potassium = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Potassium Content in (kg/ha)",
            }
        )
    )
    ph = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "pH Value",
            }
        )
    )
    rainfall = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Annual Rainfall in (mm)",
            }
        )
    )
    temperature = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Temperature in (°C)",
            }
        )
    )


class CropRecommenderForm(forms.Form):
    nitrogen = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Nitrogen Content in (kg/ha)",
            }
        )
    )
    phosphorus = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Phosphorus Content in (kg/ha)",
            }
        )
    )
    potassium = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Potassium Content in (kg/ha)",
            }
        )
    )
    temperature = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Average Temperature in (°C)",
            }
        )
    )
    humidity = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Average Humidity in (%)",
            }
        )
    )
    ph = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "pH Value",
            }
        )
    )
    rainfall = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Annual Rainfall in (mm)",
            }
        )
    )


class CropYieldPredictionForm(forms.Form):
    CROP_CHOICES = [
        ("", "Select the type of crop you'd like to grow"),
        (0, "Arecanut"),
        (1, "Arhar/Tur"),
        (2, "Castor seed"),
        (3, "Coconut "),
        (4, "Cotton(lint)"),
        (5, "Dry chillies"),
        (6, "Gram"),
        (7, "Jute"),
        (8, "Linseed"),
        (9, "Maize"),
        (10, "Mesta"),
        (11, "Niger seed"),
        (12, "Onion"),
        (13, "Other  Rabi pulses"),
        (14, "Potato"),
        (15, "Rapeseed &Mustard"),
        (16, "Rice"),
        (17, "Sesamum"),
        (18, "Small millets"),
        (19, "Sugarcane"),
        (20, "Sweet potato"),
        (21, "Tapioca"),
        (22, "Tobacco"),
        (23, "Turmeric"),
        (24, "Wheat"),
        (25, "Bajra"),
        (26, "Black pepper"),
        (27, "Cardamom"),
        (28, "Coriander"),
        (29, "Garlic"),
        (30, "Ginger"),
        (31, "Groundnut"),
        (32, "Horse-gram"),
        (33, "Jowar"),
        (34, "Ragi"),
        (35, "Cashewnut"),
        (36, "Banana"),
        (37, "Soyabean"),
        (38, "Barley"),
        (39, "Khesari"),
        (40, "Masoor"),
        (41, "Moong(Green Gram)"),
        (42, "Other Kharif pulses"),
        (43, "Safflower"),
        (44, "Sannhamp"),
        (45, "Sunflower"),
        (46, "Urad"),
        (47, "Peas & beans (Pulses)"),
        (48, "other oilseeds"),
        (49, "Other Cereals"),
        (50, "Cowpea(Lobia)"),
        (51, "Oilseeds total"),
        (52, "Guar seed"),
        (53, "Other Summer Pulses"),
        (54, "Moth"),
    ]

    STATE_CHOICES = [
        ("", "Select the state you want to predict yield"),
        (0, "Assam"),
        (1, "Karnataka"),
        (2, "Meghalaya"),
        (3, "West Bengal"),
        (4, "Puducherry"),
        (5, "Goa"),
        (6, "Kerala"),
        (7, "Andhra Pradesh"),
        (8, "Tamil Nadu"),
        (9, "Bihar"),
        (10, "Gujarat"),
        (11, "Maharashtra"),
        (12, "Mizoram"),
        (13, "Punjab"),
        (14, "Uttar Pradesh"),
        (15, "Haryana"),
        (16, "Himachal Pradesh"),
        (17, "Madhya Pradesh"),
        (18, "Tripura"),
        (19, "Nagaland"),
        (20, "Odisha"),
        (21, "Chhattisgarh"),
        (22, "Uttarakhand"),
        (23, "Jharkhand"),
        (24, "Delhi"),
        (25, "Manipur"),
        (26, "Jammu and Kashmir"),
        (27, "Telangana"),
        (28, "Arunachal Pradesh"),
        (29, "Sikkim"),
    ]

    SEASON_CHOICES = [
        ("", "Select the season you want to grow crop"),
        (1, "Autumn"),
        (2, "Summer"),
        (3, "Winter"),
        (4, "Kharif"),
        (5, "Rabi"),
        (6, "Whole Year"),
    ]

    crop = forms.ChoiceField(
        choices=CROP_CHOICES,
        widget=forms.Select(
            attrs={"class": "w-full p-2 border border-gray-300 rounded"}
        ),
    )
    state = forms.ChoiceField(
        choices=STATE_CHOICES,
        widget=forms.Select(
            attrs={"class": "w-full p-2 border border-gray-300 rounded"}
        ),
    )

    season = forms.ChoiceField(
        choices=SEASON_CHOICES,
        widget=forms.Select(
            attrs={"class": "w-full p-2 border border-gray-300 rounded"}
        ),
    )

    area = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Area in (ha)",
            }
        )
    )

    annual_rainfall = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Annual Rainfall in (mm)",
            }
        )
    )

    fertilizer_usage = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Fertilizer Usage in (kg/ha)",
            }
        )
    )

    pesticide_usage = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Pesticide Usage in (kg/ha)",
            }
        )
    )


class CustomUserCreationForm(UserCreationForm):
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
        )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
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

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user
