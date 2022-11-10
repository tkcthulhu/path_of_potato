# Generated by Django 4.1.3 on 2022-11-10 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('das_menu', '0005_menuitem_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='stock',
        ),
        migrations.CreateModel(
            name='CurrentMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.BooleanField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='das_menu.menuitem')),
            ],
        ),
    ]
