# Generated by Django 4.1.3 on 2022-11-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('das_menu', '0003_alter_menuitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
