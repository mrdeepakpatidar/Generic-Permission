# Generated by Django 3.0.7 on 2021-02-03 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210203_0521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('publish_book', 'can publish book'), ('add_author_book', 'can add author book'))},
        ),
    ]