# Generated by Django 2.1.3 on 2018-11-18 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_todolist_assigned'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(blank=True, upload_to='files')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='image_profile'),
        ),
    ]