# Generated by Django 4.0 on 2021-12-12 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_bio_alter_user_birthdate_and_more'),
        ('lists', '0002_alter_list_rooms_alter_list_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='users.user'),
        ),
    ]
