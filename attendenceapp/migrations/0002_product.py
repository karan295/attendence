# Generated by Django 2.2.5 on 2020-03-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendenceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
