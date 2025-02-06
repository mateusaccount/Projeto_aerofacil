from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from .models import Viagem

class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ['piloto','origem', 'destino', 'data_viagem', 'descricao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('origem', css_class='col-md-6'),
                Column('destino', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('data_viagem', css_class='col-md-6'),
                Column('descricao', css_class='col-md-6'),
                css_class='row'
            ),
            Submit('submit', 'Enviar', css_class='btn btn-primary')
        )
