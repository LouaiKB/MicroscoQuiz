# Generated by Django 3.0.3 on 2021-10-27 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biologicalquizapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
                ('description', models.TextField()),
                ('mode', models.CharField(max_length=255)),
                ('celltype', models.CharField(max_length=255, null=True)),
                ('components', models.CharField(max_length=255, null=True)),
                ('doi', models.CharField(max_length=255)),
                ('organism', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
