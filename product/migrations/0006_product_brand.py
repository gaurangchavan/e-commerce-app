# Generated by Django 4.2.1 on 2023-06-19 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
        ('product', '0005_alter_productimage_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='brand.brand'),
        ),
    ]
