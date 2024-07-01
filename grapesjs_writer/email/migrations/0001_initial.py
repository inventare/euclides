# Generated by Django 5.0.6 on 2024-06-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='template name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('template_code', models.TextField(blank=True, default='', verbose_name='template code')),
                ('template_id', models.CharField(max_length=150, verbose_name='template id')),
            ],
            options={
                'verbose_name': 'email template',
                'verbose_name_plural': 'email templates',
            },
        ),
    ]
