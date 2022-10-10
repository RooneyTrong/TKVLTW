# Generated by Django 3.1.4 on 2022-04-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20220330_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='numofproducts',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderdate',
            field=models.DateField(db_column='OrderDate', default='2022-04-06'),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdate',
            field=models.DateField(db_column='CreateDate', default='2022-04-06'),
        ),
    ]
