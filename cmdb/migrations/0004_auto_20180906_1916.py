# Generated by Django 2.0.7 on 2018-09-06 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20180903_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='cpu_num',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
