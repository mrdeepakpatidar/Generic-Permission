# Generated by Django 3.1.5 on 2021-01-31 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=30)),
                ('book_id', models.IntegerField()),
            ],
        ),
    ]