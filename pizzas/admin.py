from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError

from pizzas.models import Pizza
from pizzas.widgets import Select2Widget


class PizzaAdminForm(forms.ModelForm):
    class Meta:
        model = Pizza
        widgets = {
            "ingredientes": Select2Widget(
                
                choices=[
                    ("queijo", "Queijo"),
                    ("calabresa", "Calabresa"),
                    ("tomate", "Tomate"),
                    ("rucula", "Rúcula"),
                ],
            )
        }
        fields = ("nome", "ingredientes")


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    form = PizzaAdminForm
