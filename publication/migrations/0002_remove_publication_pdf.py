# Generated by Django 5.1.1 on 2024-09-08 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='pdf',
        ),
    ]
