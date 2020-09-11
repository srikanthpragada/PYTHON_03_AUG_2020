from django import forms


class SalaryUpdateForm(forms.Form):
    # Fields
    id = forms.IntegerField(required=True, label="Employee Id")
    salary = forms.IntegerField(required=True, label = "New Salary", min_value=50000)


