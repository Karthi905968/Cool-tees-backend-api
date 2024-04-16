# Generated by Django 5.0.1 on 2024-04-10 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='body',
            field=models.TextField(blank=True, db_index=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=100, null=True, verbose_name='Name'),
        ),
    ]
