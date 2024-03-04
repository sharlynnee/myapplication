# Generated by Django 5.0.2 on 2024-02-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0003_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
