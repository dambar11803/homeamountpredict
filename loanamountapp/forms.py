from django import forms
from .models import ClientDetails 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

class ClientDetailsForm(forms.ModelForm):
    class Meta: 
        model = ClientDetails 
        fields = ['name','sex','marital','age','salary','family_income','home_value','tenure','interest']  
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-5 mb-0'),
                Column('sex', css_class='form-group col-md-5 mb-0'),
                Column('marital', css_class='form-group col-md-5 mb-0'),
                Column('age', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('salary', css_class='form-group col-md-5 mb-0'),
                Column('family_income', css_class='form-group col-md-5 mb-0'),
                Column('home_value', css_class='form-group col-md-5 mb-0'),
                 Column('tenure', css_class='form-group col-md-5 mb-0'),
                Column('interest', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )   
        
       
        
    
        
       
            