# Generated by Django 3.1.7 on 2021-08-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0022_questionnaire_shownumbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='showNumbers',
            field=models.BooleanField(default=True, null=True),
        ),
    ]