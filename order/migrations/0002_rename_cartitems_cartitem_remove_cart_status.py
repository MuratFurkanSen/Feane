# Generated by Django 5.0.3 on 2024-03-17 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_rename_name_category_title_alter_item_slug'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItems',
            new_name='CartItem',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='status',
        ),
    ]
