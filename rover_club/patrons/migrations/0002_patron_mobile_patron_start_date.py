# Generated by Django 4.2.1 on 2023-06-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patron',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patron',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
