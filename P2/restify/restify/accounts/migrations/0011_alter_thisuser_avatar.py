# Generated by Django 4.1.7 on 2023-03-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_thisuser_password1_alter_thisuser_password2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thisuser',
            name='avatar',
            field=models.ImageField(blank=True, default='..default_user.png', null=True, upload_to='avatar'),
        ),
    ]
