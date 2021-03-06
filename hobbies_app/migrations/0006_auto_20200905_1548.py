# Generated by Django 3.1 on 2020-09-05 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hobbies_app', '0005_auto_20200901_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='activity date')),
            ],
        ),
        migrations.AddField(
            model_name='hobby',
            name='friends',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hobbies_app.friend'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='friend',
            name='friendship',
            field=models.CharField(choices=[('Old', 'OLD FRIEND'), ('Close', 'CLOSE FRIEND'), ('Good', 'GOOD FRIEND'), ('New', 'NEW FRIEND')], default='New', max_length=100),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_color', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hobby',
            name='activities',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hobbies_app.activity'),
            preserve_default=False,
        ),
    ]
