# Generated by Django 2.1.4 on 2019-03-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20190324_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='stories',
            field=models.CharField(blank=True, help_text='put *% between each story', max_length=500),
        ),
    ]
