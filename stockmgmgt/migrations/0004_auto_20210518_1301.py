# Generated by Django 3.2 on 2021-05-18 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmgt', '0003_alter_stock_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='export_to_CSV',
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stockmgmgt.category'),
        ),
    ]
