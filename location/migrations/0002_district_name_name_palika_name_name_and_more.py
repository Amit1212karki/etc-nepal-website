# Generated by Django 5.1.1 on 2024-10-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='name_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='palika',
            name='name_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='name_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
