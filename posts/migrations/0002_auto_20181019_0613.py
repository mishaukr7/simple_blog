# Generated by Django 2.0 on 2018-10-19 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='upload/default.jpg', upload_to='upload'),
        ),
    ]