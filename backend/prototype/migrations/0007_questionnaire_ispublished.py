# Generated by Django 3.1.7 on 2021-08-22 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0006_choicequestion_ismulti'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='isPublished',
            field=models.BinaryField(default=False, null=True),
        ),
    ]
