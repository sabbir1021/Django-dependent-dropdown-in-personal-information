# Generated by Django 3.1.1 on 2020-09-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependent', '0007_auto_20200926_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.FileField(upload_to='person image'),
        ),
    ]
