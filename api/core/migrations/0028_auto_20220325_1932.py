# Generated by Django 3.1.4 on 2022-03-25 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20220324_2110'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.RemoveField(
            model_name='cartdetails',
            name='img',
        ),
        migrations.RemoveField(
            model_name='cartdetails',
            name='price',
        ),
        migrations.RemoveField(
            model_name='cartdetails',
            name='productname',
        ),
        migrations.RemoveField(
            model_name='cartdetails',
            name='username',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='img',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='productname',
        ),
        migrations.AddField(
            model_name='cartdetails',
            name='cartid',
            field=models.ForeignKey(db_column='CartID', default=-1, on_delete=django.db.models.deletion.DO_NOTHING, to='core.cart'),
        ),
        migrations.AddField(
            model_name='cartdetails',
            name='productcode',
            field=models.ForeignKey(db_column='ProductCode', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.product'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='productcode',
            field=models.ForeignKey(db_column='ProductCode', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.product'),
        ),
        migrations.AddField(
            model_name='profile',
            name='defaultaddress',
            field=models.CharField(blank=True, db_column='DefaultAddress', max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phonenum',
            field=models.CharField(blank=True, db_column='PhoneNum', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='img',
            field=models.CharField(blank=True, db_column='IMG', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cartdetails',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='orderid',
            field=models.ForeignKey(db_column='OrderID', on_delete=django.db.models.deletion.DO_NOTHING, to='core.orders'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderaddress',
            field=models.CharField(db_column='OrderAddress', default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderdate',
            field=models.DateField(db_column='OrderDate', default='2022-03-25'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderstatus',
            field=models.IntegerField(db_column='OrderStatus', default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total',
            field=models.FloatField(db_column='Total', default=0.0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdate',
            field=models.DateField(db_column='CreateDate', default='2022-03-25'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.CharField(db_column='IMG', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.CharField(db_column='IMG', max_length=200),
        ),
        migrations.AlterModelTable(
            name='brand',
            table='core_brand',
        ),
        migrations.AlterModelTable(
            name='cart',
            table='core_cart',
        ),
        migrations.AlterModelTable(
            name='cartdetails',
            table='core_cartdetails',
        ),
        migrations.AlterModelTable(
            name='feedback',
            table='core_feedback',
        ),
        migrations.AlterModelTable(
            name='orderdetails',
            table='core_orderdetails',
        ),
        migrations.AlterModelTable(
            name='orders',
            table='core_orders',
        ),
        migrations.AlterModelTable(
            name='product',
            table='core_product',
        ),
        migrations.AlterModelTable(
            name='profile',
            table='core_profile',
        ),
    ]
