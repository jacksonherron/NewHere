# Generated by Django 2.2.4 on 2019-08-08 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friendly', '0003_auto_20190808_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validate', models.BooleanField(default=False)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('user_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_matches', to='friendly.Profile')),
                ('user_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_matches', to='friendly.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='friendly.Profile')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='friendly.Match')),
            ],
        ),
    ]