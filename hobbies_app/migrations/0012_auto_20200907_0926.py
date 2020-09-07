# Generated by Django 3.1 on 2020-09-07 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hobbies_app', '0011_auto_20200905_1944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='activity',
            name='people',
        ),
        migrations.RemoveField(
            model_name='hobby',
            name='activities',
        ),
        migrations.AddField(
            model_name='activity',
            name='hobby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hobbies_app.hobby'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hobby',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='hobby',
            name='friends',
        ),
        migrations.AddField(
            model_name='hobby',
            name='friends',
            field=models.ManyToManyField(to='hobbies_app.Friend'),
        ),
    ]
