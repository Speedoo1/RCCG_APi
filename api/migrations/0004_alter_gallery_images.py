# Generated by Django 3.2.19 on 2023-09-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20230911_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='images',
            field=models.ImageField(upload_to=''),
        ),
    ]