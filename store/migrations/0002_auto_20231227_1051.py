# Generated by Django 3.2.23 on 2023-12-27 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='category',
            name='store_categ_name_1278fd_idx',
        ),
        migrations.RemoveIndex(
            model_name='category',
            name='store_categ_is_dele_bbc986_idx',
        ),
    ]
