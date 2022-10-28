from dataclasses import field, fields
from socket import fromshare
from django import forms
from reservas_app.models import reserva
class formreservas(forms.ModelForm):
    class Meta:
        model = reserva
        fields = '__all__'