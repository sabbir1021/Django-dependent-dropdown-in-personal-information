from django import forms
from .models import Person , SubDistrict , District , Division , Country

class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['division'].queryset = Division.objects.none()
        self.fields['district'].queryset = District.objects.none()
        self.fields['subdistrict'].queryset = SubDistrict.objects.none()

        if True:
            if 'country' in self.data:
                try:
                    country_id = int(self.data.get('country'))
                    self.fields['division'].queryset = Division.objects.filter(country_id=country_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['division'].queryset = self.instance.country
        
        if True:
            if 'division' in self.data:
                try:
                    division_id = int(self.data.get('division'))
                    self.fields['district'].queryset = District.objects.filter(division_id=division_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['district'].queryset = self.instance.country.district_set.order_by('name')

        if True:
            if 'district' in self.data:
                try:
                    district_id = int(self.data.get('district'))
                    self.fields['subdistrict'].queryset = SubDistrict.objects.filter(district_id=district_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['subdistrict'].queryset = self.instance.country.subdistrict_set.order_by('name')
    


class PersonFilterForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['country','division','district','subdistrict']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['division'].queryset = Division.objects.none()
        self.fields['district'].queryset = District.objects.none()
        self.fields['subdistrict'].queryset = SubDistrict.objects.none()

        if True:
            if 'country' in self.data:
                try:
                    country_id = int(self.data.get('country'))
                    self.fields['division'].queryset = Division.objects.filter(country_id=country_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['division'].queryset = self.instance.country
        
        if True:
            if 'division' in self.data:
                try:
                    division_id = int(self.data.get('division'))
                    self.fields['district'].queryset = District.objects.filter(division_id=division_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['district'].queryset = self.instance.country.district_set.order_by('name')

        if True:
            if 'district' in self.data:
                try:
                    district_id = int(self.data.get('district'))
                    self.fields['subdistrict'].queryset = SubDistrict.objects.filter(district_id=district_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['subdistrict'].queryset = self.instance.country.subdistrict_set.order_by('name')


class PersonupdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'