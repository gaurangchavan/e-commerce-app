# Generated by Django 4.2.1 on 2023-05-26 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='covee_image',
            new_name='cover_image',
        ),
    ]
