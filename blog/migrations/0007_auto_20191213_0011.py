# Generated by Django 2.2.7 on 2019-12-12 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='static/media'),
        ),
    ]