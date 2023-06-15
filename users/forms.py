from django import forms

class UserInputForm(forms.Form):
    def __init__(self, *args, **kwargs):
        placeholders = kwargs.pop('placeholders')
        super(UserInputForm, self).__init__(*args, **kwargs)
        for placeholder in placeholders:
            self.fields[placeholder.name] = forms.CharField(label=placeholder.name)
