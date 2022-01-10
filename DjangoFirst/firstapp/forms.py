from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label = "Имя", initial = "John", min_length=2, max_length=20)
    age = forms.IntegerField(label = "Годики", required=False, max_value=100)
    #comment = forms.CharField(label="Комментарий", widget=forms.Textarea, help_text="расскажите как прошел ваш день")
    #accept = forms.NullBooleanField()
    #field_order = ["name","age", "accept"]


