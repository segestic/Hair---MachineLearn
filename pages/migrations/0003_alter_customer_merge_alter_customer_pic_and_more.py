# Generated by Django 4.0.4 on 2022-04-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_customer_merge_alter_customer_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='merge',
            field=models.ImageField(max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pic',
            field=models.ImageField(max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='style',
            field=models.ImageField(max_length=255, null=True, upload_to=''),
        ),
    ]
