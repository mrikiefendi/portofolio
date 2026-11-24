from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, default="M RIKI EFENDI")
    role = models.CharField(
        max_length=180, default="Informatics Student • Visual Developer"
    )
    tagline = models.TextField(
        blank=True, default="Building digital solutions with logic and creativity."
    )
    photo = models.ImageField(upload_to="profile/", blank=True, null=True)
    email = models.EmailField(blank=True)
    whatsapp = models.CharField(max_length=40, blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    class Meta:
        verbose_name = "Profil"

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=80, blank=True, default="Technology")
    icon_text = models.CharField(
        max_length=12, blank=True, help_text="Teks/icon pendek, misalnya JS"
    )
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order", "name")


class Project(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    technologies = models.CharField(max_length=250, blank=True)
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order", "-id")


class Education(models.Model):
    institution = models.CharField(max_length=150)
    program = models.CharField(max_length=150, blank=True)
    period = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.institution

    class Meta:
        ordering = ("order", "-id")


class Experience(models.Model):
    position = models.CharField(max_length=150)
    organization = models.CharField(max_length=150, blank=True)
    period = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position

    class Meta:
        ordering = ("order", "-id")


class Leadership(models.Model):
    position = models.CharField(max_length=150)
    organization = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position

    class Meta:
        ordering = ("order", "-id")