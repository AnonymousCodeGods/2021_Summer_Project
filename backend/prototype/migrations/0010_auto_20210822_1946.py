# Generated by Django 3.1.7 on 2021-08-22 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0009_auto_20210822_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='NAID',
        ),
        migrations.AddField(
            model_name='answer',
            name='CMPID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prototype.complition'),
        ),
    ]