# Generated by Django 3.0.2 on 2020-09-16 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_periodtable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='presents_cls',
            new_name='present_cls',
        ),
        migrations.AlterField(
            model_name='attendence',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
