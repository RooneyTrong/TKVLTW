# Generated by Django 3.1.4 on 2022-04-15 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_remove_feedback_unread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='productcode',
            field=models.ForeignKey(db_column='ProductID', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderdate',
            field=models.DateField(db_column='OrderDate', default='2022-04-15'),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdate',
            field=models.DateField(db_column='CreateDate', default='2022-04-15'),
        ),
    ]
