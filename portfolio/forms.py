from django import forms

from .models import (
    Education,
    Experience,
    Leadership,
    Profile,
    Project,
    Skill,
)


class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check"


class ProfileForm(StyledModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class SkillForm(StyledModelForm):
    class Meta:
        model = Skill
        fields = "__all__"


class ProjectForm(StyledModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class EducationForm(StyledModelForm):
    class Meta:
        model = Education
        fields = "__all__"


class ExperienceForm(StyledModelForm):
    class Meta:
        model = Experience
        fields = "__all__"


class LeadershipForm(StyledModelForm):
    class Meta:
        model = Leadership
        fields = "__all__"