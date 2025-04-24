from django import forms
from .models import students_records

class students_recordsForm(forms.ModelForm):
    class Meta:
        model = students_records
        fields = ['stu_id', 'name', 'course', 'address']
        widgets = {
            'stu_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}), 
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }