# Generated by Django 3.1 on 2020-09-05 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies_app', '0006_auto_20200905_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hobbies_app.hobby')),
            ],
        ),
    ]
