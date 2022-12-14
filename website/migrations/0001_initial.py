# Generated by Django 3.2.6 on 2022-07-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=300)),
                ('desc', models.CharField(max_length=300)),
                ('posted_by', models.CharField(max_length=100)),
                ('post_date', models.DateField()),
                ('price', models.IntegerField()),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]
