from django import forms


class IntegerField(forms.IntegerField):
    pass


class BooleanField(forms.BooleanField):
    pass


class UserInputForm(forms.Form):
    FIELD_TYPES = {
        'company_registration_number': IntegerField,
        'company_shareholder_count': BooleanField
        # Add more field mappings as needed
    }

    def __init__(self, *args, **kwargs):
        placeholders = kwargs.pop('placeholders')
        super(UserInputForm, self).__init__(*args, **kwargs)
        for placeholder in placeholders:
            field_type = self.FIELD_TYPES.get(placeholder.name, forms.CharField)
            self.fields[placeholder.name] = field_type(label=placeholder.name)

        # Add default CharField for fields not defined in the mapping
        for field_name, field in self.fields.items():
            if not isinstance(field, forms.Field):
                self.fields[field_name] = forms.CharField(label=field_name)

