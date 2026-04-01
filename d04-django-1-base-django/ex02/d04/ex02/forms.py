from django import forms


class InputForm(forms.Form):
    text_ipt = forms.CharField(label="Text input")
