# Generated by Django 2.2.9 on 2020-04-21 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200420_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default='No Name Provided', max_length=150),
            preserve_default=False,
        ),
    ]
