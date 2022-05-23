from django.forms import ModelForm
from app.models import Carros


# Create the form class.
class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['seller_id', 'seller_zip_code_prefix', 'seller_city', 'seller_state']
