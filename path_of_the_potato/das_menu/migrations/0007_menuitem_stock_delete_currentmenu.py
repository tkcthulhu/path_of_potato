# Generated by Django 4.1.3 on 2022-11-10 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('das_menu', '0006_remove_menuitem_stock_currentmenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='stock',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CurrentMenu',
        ),
    ]
