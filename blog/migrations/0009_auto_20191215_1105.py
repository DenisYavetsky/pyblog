# Generated by Django 2.2.7 on 2019-12-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191214_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='static/media'),
        ),
    ]