# Generated by Django 3.1.7 on 2021-03-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0161_auto_20210316_2004"),
    ]

    operations = [
        migrations.AddField(
            model_name="nimbuschangelog",
            name="new_publish_status",
            field=models.CharField(
                choices=[
                    ("Idle", "Idle"),
                    ("Review", "Review"),
                    ("Approved", "Approved"),
                    ("Waiting", "Waiting"),
                ],
                default="Idle",
                max_length=255,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="nimbuschangelog",
            name="old_publish_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Idle", "Idle"),
                    ("Review", "Review"),
                    ("Approved", "Approved"),
                    ("Waiting", "Waiting"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="nimbusexperiment",
            name="publish_status",
            field=models.CharField(
                choices=[
                    ("Idle", "Idle"),
                    ("Review", "Review"),
                    ("Approved", "Approved"),
                    ("Waiting", "Waiting"),
                ],
                default="Idle",
                max_length=255,
            ),
        ),
    ]