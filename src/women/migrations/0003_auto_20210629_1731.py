# Generated by Django 3.2 on 2021-06-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_auto_20210611_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='women',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='women',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
