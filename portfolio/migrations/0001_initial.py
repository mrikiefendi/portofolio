from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = ()

    operations = (
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("institution", models.CharField(max_length=150)),
                ("program", models.CharField(blank=True, max_length=150)),
                ("period", models.CharField(blank=True, max_length=60)),
                ("description", models.TextField(blank=True)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={
                "ordering": ["order", "-id"],
            },
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.CharField(max_length=150)),
                ("organization", models.CharField(blank=True, max_length=150)),
                ("period", models.CharField(blank=True, max_length=60)),
                ("description", models.TextField(blank=True)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={
                "ordering": ["order", "-id"],
            },
        ),
        migrations.CreateModel(
            name="Leadership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.CharField(max_length=150)),
                ("organization", models.CharField(blank=True, max_length=150)),
                ("description", models.TextField(blank=True)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={
                "ordering": ["order", "-id"],
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="Huda Muliya", max_length=100)),
                (
                    "role",
                    models.CharField(
                        default="Informatics Student • Visual Developer", max_length=180
                    ),
                ),
                (
                    "tagline",
                    models.TextField(
                        blank=True,
                        default="Building digital solutions with logic and creativity.",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="profile/"),
                ),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("whatsapp", models.CharField(blank=True, max_length=40)),
                ("instagram", models.URLField(blank=True)),
                ("linkedin", models.URLField(blank=True)),
                ("github", models.URLField(blank=True)),
            ],
            options={
                "verbose_name": "Profil",
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=120)),
                ("category", models.CharField(blank=True, max_length=100)),
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="projects/"),
                ),
                ("technologies", models.CharField(blank=True, max_length=250)),
                ("url", models.URLField(blank=True)),
                ("order", models.PositiveIntegerField(default=0)),
                ("is_featured", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["order", "-id"],
            },
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=80)),
                (
                    "category",
                    models.CharField(blank=True, default="Technology", max_length=80),
                ),
                (
                    "icon_text",
                    models.CharField(
                        blank=True,
                        help_text="Teks/icon pendek, misalnya JS",
                        max_length=12,
                    ),
                ),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={
                "ordering": ["order", "name"],
            },
        ),
    )