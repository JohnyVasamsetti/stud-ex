# Generated by Django 3.0.2 on 2020-09-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FolderModel',
            fields=[
                ('FolderID', models.IntegerField(primary_key=True, serialize=False)),
                ('FolderName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('SubjectID', models.IntegerField(primary_key=True, serialize=False)),
                ('SubjectName', models.CharField(max_length=200)),
            ],
        ),
    ]
