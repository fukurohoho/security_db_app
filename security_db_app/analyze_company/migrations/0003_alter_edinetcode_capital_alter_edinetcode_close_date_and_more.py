# Generated by Django 5.0.1 on 2024-01-06 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze_company', '0002_alter_edinetcode_link_or_not'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edinetcode',
            name='capital',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='edinetcode',
            name='close_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='edinetcode',
            name='stock_code',
            field=models.IntegerField(null=True),
        ),
    ]
