# Generated by Django 3.0.2 on 2020-09-04 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_attendence'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='totla_cls',
            new_name='total_cls',
        ),
    ]
