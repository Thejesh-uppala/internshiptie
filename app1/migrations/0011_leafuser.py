# Generated by Django 4.0.4 on 2022-06-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_delete_leafuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeafUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Service', models.EmailField(max_length=50)),
                ('Status', models.CharField(max_length=50)),
                ('Phonenumber', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Confirmpassword', models.CharField(max_length=50)),
            ],
        ),
    ]
