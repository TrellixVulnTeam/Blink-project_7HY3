# Generated by Django 2.1.4 on 2019-03-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20190322_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_cover',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
