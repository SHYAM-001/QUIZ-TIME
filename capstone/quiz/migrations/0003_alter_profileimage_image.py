# Generated by Django 4.2.5 on 2023-10-05 14:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_profileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimage',
            name='image',
            field=models.ImageField(blank=True, default='quiz/default.jpg', null=True, upload_to='quiz/photos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], verbose_name='Profile Image'),
        ),
    ]