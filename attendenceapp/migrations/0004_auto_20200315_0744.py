# Generated by Django 2.2.5 on 2020-03-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendenceapp', '0003_auto_20200315_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]