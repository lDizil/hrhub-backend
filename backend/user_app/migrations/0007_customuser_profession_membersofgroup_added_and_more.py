# Generated by Django 5.0.6 on 2024-07-16 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0006_remove_membersofgroup_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profession',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='membersofgroup',
            name='added',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='membersofgroup',
            name='chat_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='membersofgroup',
            name='service_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
