# Generated by Django 3.2.7 on 2021-09-14 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlapp', '0007_alter_feature_lnk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='lnk',
            field=models.CharField(default="\\{% url 'login' %\\}", max_length=20),
        ),
    ]
