# Generated by Django 2.2.4 on 2019-08-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendly', '0005_profile_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.PositiveIntegerField(),
        ),
    ]