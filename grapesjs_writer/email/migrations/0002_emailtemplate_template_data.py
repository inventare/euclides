# Generated by Django 5.0.6 on 2024-06-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='template_data',
            field=models.JSONField(default={}, verbose_name='template data'),
        ),
    ]
