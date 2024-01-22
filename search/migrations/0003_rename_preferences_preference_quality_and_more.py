# Generated by Django 5.0.1 on 2024-01-22 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_preference_delete_preferences'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preference',
            old_name='preferences',
            new_name='quality',
        ),
        migrations.AddField(
            model_name='preference',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=20),
        ),
    ]
