# Generated by Django 3.1.7 on 2021-08-29 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0036_auto_20210829_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='belongto',
            name='order',
            field=models.ImageField(default=-1, null=True, upload_to=''),
        ),
    ]