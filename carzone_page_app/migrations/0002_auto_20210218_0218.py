# Generated by Django 3.1.6 on 2021-02-17 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carzone_page_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='photo',
            field=models.ImageField(upload_to='team_pic/Y%/m%/d%/'),
        ),
    ]
