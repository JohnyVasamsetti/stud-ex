# Generated by Django 3.0.2 on 2020-09-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200904_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodTable',
            fields=[
                ('period', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('teacher', models.CharField(max_length=30)),
            ],
        ),
    ]
