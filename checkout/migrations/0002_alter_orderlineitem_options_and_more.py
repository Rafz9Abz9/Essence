# Generated by Django 5.0.1 on 2024-02-23 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderlineitem',
            options={'verbose_name_plural': 'OrderLineItems'},
        ),
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='Product',
            new_name='product',
        ),
    ]
