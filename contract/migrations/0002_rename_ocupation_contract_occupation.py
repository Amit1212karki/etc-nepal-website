# Generated by Django 5.1.1 on 2024-09-27 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='ocupation',
            new_name='occupation',
        ),
    ]
