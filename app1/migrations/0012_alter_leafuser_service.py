# Generated by Django 4.0.4 on 2022-06-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_leafuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leafuser',
            name='Service',
            field=models.CharField(max_length=50),
        ),
    ]