# Generated by Django 3.2.7 on 2021-10-02 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_c'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='c',
        ),
    ]
