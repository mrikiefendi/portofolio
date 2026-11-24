from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    EducationForm,
    ExperienceForm,
    LeadershipForm,
    ProfileForm,
    ProjectForm,
    SkillForm,
)
from .models import (
    Education,
    Experience,
    Leadership,
    Profile,
    Project,
    Skill,
)


def home(request):
    profile = Profile.objects.first()
    return render(
        request,
        "portfolio/home.html",
        {
            "profile": profile,
            "skills": Skill.objects.all(),
            "projects": Project.objects.filter(is_featured=True),
            "education": Education.objects.all(),
            "experiences": Experience.objects.all(),
            "leadership": Leadership.objects.all(),
        },
    )

@login_required
def dashboard(request):
    stats = [
        ("Projects", Project.objects.count(), "projects"),
        ("Skills", Skill.objects.count(), "skills"),
        ("Education", Education.objects.count(), "education"),
        ("Experience", Experience.objects.count(), "experience"),
        ("Leadership", Leadership.objects.count(), "leadership"),
    ]
    return render(request, "portfolio/dashboard.html", {"stats": stats})

MODEL_MAP = {
    "profile": (Profile, ProfileForm, "Profil"),
    "skills": (Skill, SkillForm, "Skill"),
    "projects": (Project, ProjectForm, "Project"),
    "education": (Education, EducationForm, "Education"),
    "experience": (Experience, ExperienceForm, "Experience"),
    "leadership": (Leadership, LeadershipForm, "Leadership"),
}

@login_required
def manage_items(request, section):
    if section not in MODEL_MAP:
        return redirect("dashboard")
    model, _form_class, label = MODEL_MAP[section]
    items = model.objects.all()
    return render(
        request,
        "portfolio/manage.html",
        {"items": items, "section": section, "label": label},
    )


@login_required
def edit_item(request, section, pk=None):
    if section not in MODEL_MAP:
        return redirect("dashboard")
    model, form_class, label = MODEL_MAP[section]
    instance = get_object_or_404(model, pk=pk) if pk else None
    form = form_class(request.POST or None, request.FILES or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"{label} berhasil disimpan.")
        return redirect("manage", section=section)
    return render(
        request,
        "portfolio/edit.html",
        {"form": form, "label": label, "section": section, "instance": instance},
    )


@login_required
def delete_item(request, section, pk):
    if section not in MODEL_MAP:
        return redirect("dashboard")
    model, _, label = MODEL_MAP[section]
    item = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        item.delete()
        messages.success(request, f"{label} berhasil dihapus.")
        return redirect("manage", section=section)
    return render(request, "portfolio/delete.html", {"item": item, "section": section})