from django import forms

class TestForm(forms.Form):
    name = forms.CharField(label="姓名", max_length=10, widget=forms.TextInput)
    age = forms.IntegerField(max_value=200, min_value=1, label="年龄")
    