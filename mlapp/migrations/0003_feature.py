# Generated by Django 3.2.2 on 2021-09-10 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlapp', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('describtion', models.CharField(max_length=500)),
            ],
        ),
    ]