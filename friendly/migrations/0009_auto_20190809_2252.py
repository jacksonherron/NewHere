# Generated by Django 2.2.4 on 2019-08-09 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendly', '0008_auto_20190809_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='time_stamp',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='time_stamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
