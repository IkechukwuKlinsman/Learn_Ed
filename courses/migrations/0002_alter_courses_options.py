# Generated by Django 4.2.2 on 2023-07-01 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['title'], 'verbose_name_plural': 'Courses'},
        ),
    ]
