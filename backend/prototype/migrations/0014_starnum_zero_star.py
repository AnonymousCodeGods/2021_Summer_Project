# Generated by Django 3.1.7 on 2021-08-22 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0013_auto_20210822_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='starnum',
            name='zero_star',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
