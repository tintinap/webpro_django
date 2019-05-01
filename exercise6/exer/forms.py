from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from .models import Dayoff

import datetime

class LeaveModelForm(forms.ModelForm):
    # approve_status = forms.ChoiceField(widget=forms.HiddenInput, required=False, initial='w8')
    date_start = forms.DateField(initial='dd/mm/yyyy', input_formats=['%d/%m/%Y'])
    date_end = forms.DateField(initial='dd/mm/yyyy', input_formats=['%d/%m/%Y'])

    class Meta:
        model = Dayoff
        exclude = ['create_by', 'approve_status']

    def clean_date_start(self):
        data = self.cleaned_data['date_start']
        if data < datetime.date.today():
            raise forms.ValidationError('ไม่สามารถเลือกวันในอดีตได้')
        return data

    def clean_date_end(self):
        data = self.cleaned_data['date_end']
        if data < datetime.date.today():
            raise forms.ValidationError('ไม่สามารถเลือกวันในอดีตได้')
        return data

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('date_start')
        end = cleaned_data.get('date_end')

        if str(end) < str(start):
            self.add_error('date_start', 'วันไม่ถูกต้อง')
            self.add_error('date_end', 'วันไม่ถูกต้อง')
