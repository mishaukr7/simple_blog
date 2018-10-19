# Generated by Django 2.1.2 on 2018-10-18 17:54

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181018_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='country', chained_model_field='country', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.City'),
        ),
    ]
