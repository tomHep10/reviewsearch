# Generated by Django 5.0.1 on 2024-01-22 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferences', models.CharField(choices=[('AU', 'Audio'), ('MC', 'Microphone')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Preferences',
        ),
    ]
