# Generated by Django 5.0.1 on 2024-02-25 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_orderlineitem_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='line_items',
            field=models.ManyToManyField(blank=True, related_name='orders', to='checkout.orderlineitem'),
        ),
    ]