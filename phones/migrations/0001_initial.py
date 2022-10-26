# Generated by Django 4.1.2 on 2022-10-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=100)),
                ('release_date', models.DateField(max_length=10)),
                ('lte_exists', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
        ),
    ]
