# Generated by Django 2.2.5 on 2020-03-17 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendenceapp', '0004_auto_20200315_0744'),
    ]

    operations = [
        migrations.CreateModel(
            name='product1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]
