from django.forms import ModelForm
from .models import User


# Create the User Registration Form
class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
