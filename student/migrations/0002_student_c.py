# Generated by Django 3.2.7 on 2021-10-02 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='c',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
