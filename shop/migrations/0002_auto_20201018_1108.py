# Generated by Django 3.0.10 on 2020-10-18 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='update',
            new_name='updated',
        ),
    ]
