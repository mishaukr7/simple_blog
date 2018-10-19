from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Country, City
from smart_selects.form_fields import ChainedModelChoiceField


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    user_country = forms.ModelChoiceField(queryset=Country.objects.all())
    birthday = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    user_city = ChainedModelChoiceField(
        queryset=City.objects.all(),
        to_app_name='accounts',
        to_model_name='City',
        chained_field='user_country',
        chained_model_field='country',
        foreign_key_app_name='accounts',
        foreign_key_model_name='Profile',
        foreign_key_field_name='user_city',
        show_all=False,
        auto_choose=False,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'birthday', 'user_country', 'user_city')


class ProfileAdminForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
