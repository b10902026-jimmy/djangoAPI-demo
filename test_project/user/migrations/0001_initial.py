# Generated by Django 4.1.4 on 2022-12-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
