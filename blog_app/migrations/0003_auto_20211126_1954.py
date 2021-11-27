# Generated by Django 3.2.8 on 2021-11-26 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0002_auto_20211126_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.TextField(choices=[('math', 'Math'), ('history', 'History'), ('technology', 'Technology')], default='history'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publisher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.CharField(max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]