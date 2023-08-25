# Generated by Django 4.0.5 on 2022-06-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kotirghorapp', '0002_alter_item_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='owner',
            new_name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
