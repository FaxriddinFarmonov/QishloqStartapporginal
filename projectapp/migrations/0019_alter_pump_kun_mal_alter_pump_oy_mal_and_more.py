# Generated by Django 4.2.1 on 2023-05-12 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0018_rename_yil_mal_pump_umumiy_mal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pump',
            name='kun_mal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pump',
            name='oy_mal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pump',
            name='soat_mal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pump',
            name='umumiy_mal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]