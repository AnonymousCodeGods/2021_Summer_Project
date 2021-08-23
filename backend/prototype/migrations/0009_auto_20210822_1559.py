# Generated by Django 3.1.7 on 2021-08-22 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0008_auto_20210822_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='isPublished',
            field=models.BooleanField(default=False, null=True),
        ),
    ]