# Generated by Django 3.2.25 on 2024-06-29 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vvvapp', '0002_adduser_ischecked'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adduser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='adduser',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
