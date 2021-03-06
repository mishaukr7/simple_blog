# Generated by Django 2.1.2 on 2018-10-18 17:10

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_email_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, show_all=True, to='accounts.City'),
        ),
    ]
