# Generated by Django 2.2.2 on 2019-12-25 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20191213_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_hot',
            field=models.BooleanField(default=False, verbose_name='горячий продукт'),
        ),
    ]