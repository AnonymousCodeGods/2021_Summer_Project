# Generated by Django 3.1.7 on 2021-08-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0025_auto_20210827_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choicequestion',
            name='limitNum',
        ),
        migrations.RemoveField(
            model_name='complition',
            name='limitNum',
        ),
        migrations.RemoveField(
            model_name='locationquestion',
            name='limitNum',
        ),
        migrations.AddField(
            model_name='choicequestion',
            name='hasLimitNum',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='complition',
            name='hasLimitNum',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='locationquestion',
            name='hasLimitNum',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
