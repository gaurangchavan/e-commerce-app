# Generated by Django 4.2.1 on 2023-05-30 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_slug_alter_producttag_slug'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='variation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productvariation'),
        ),
    ]
