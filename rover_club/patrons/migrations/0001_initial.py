# Generated by Django 4.2.1 on 2023-06-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('mname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
            ],
        ),
    ]
