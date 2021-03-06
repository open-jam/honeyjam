# Generated by Django 2.2.15 on 2020-08-17 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import libs.django.db.models.base_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('gag_type', models.IntegerField(choices=[(0, '문답형')], default=0, verbose_name='개그 타입')),
                ('question', models.TextField(blank=True, null=True, verbose_name='문')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='답')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_gag', to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
            options={
                'verbose_name': '개그',
                'verbose_name_plural': '개그 목록',
                'db_table': 'gag',
            },
            bases=(libs.django.db.models.base_model.ChangeMixin, models.Model),
        ),
    ]
