# Generated by Django 4.1.7 on 2023-03-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
