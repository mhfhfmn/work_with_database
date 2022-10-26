# Generated by Django 4.1.2 on 2022-10-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.URLField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.PositiveIntegerField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(verbose_name='release_date'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=125, null=True, unique=True),
        ),
    ]
