# Generated by Django 3.2.2 on 2021-09-12 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlapp', '0004_rename_describtion_feature_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='ml_img',
            field=models.ImageField(default='images/0.jpg', upload_to='model_cover_pic'),
        ),
    ]
