# Generated by Django 3.1.7 on 2021-08-21 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0004_auto_20210821_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='choicequestion',
            name='FOID',
            field=models.IntegerField(null=True),
        ),
    ]