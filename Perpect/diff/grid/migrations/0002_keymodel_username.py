# Generated by Django 2.2.7 on 2019-12-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='keymodel',
            name='username',
            field=models.CharField(default='o', max_length=30),
            preserve_default=False,
        ),
    ]
