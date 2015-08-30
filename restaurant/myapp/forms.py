from django.forms import ModelForm
from django import forms
from .models import Receta

class RecetaForm(ModelForm):
	class Meta:
		model = Receta
		fields = "__all__"


