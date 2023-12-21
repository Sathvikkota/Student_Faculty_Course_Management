from django import forms
from .models import Faculty

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields="__all__"
        exclude={"password"}
        labels={"facultyid":"Enter Faculty ID","fullname":"Faculty Name","gender":"Select Gender","department":"Select Department",
                "qualification":"Select Qualification","designation":"Select Designation"}

