# Generated by Django 3.1.7 on 2021-08-29 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0031_auto_20210829_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chanswer',
            name='content',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cmpanswer',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='loanswer',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
