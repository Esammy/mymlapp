# Generated by Django 3.2.2 on 2021-09-10 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mlapp', '0003_feature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='describtion',
            new_name='description',
        ),
    ]