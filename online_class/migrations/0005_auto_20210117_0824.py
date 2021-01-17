# Generated by Django 3.1.5 on 2021-01-17 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_class', '0004_auto_20210117_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassConfirmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_confirmed_class_id', to='online_class.class')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_confirmed_user_id', to='online_class.user')),
            ],
        ),
        migrations.DeleteModel(
            name='ClassBooked',
        ),
    ]