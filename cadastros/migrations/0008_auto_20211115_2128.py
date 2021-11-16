# Generated by Django 3.2.8 on 2021-11-16 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0007_doadores_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doadores',
            old_name='usuario',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='doacao',
            name='usuario',
        ),
        migrations.AddField(
            model_name='doacao',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
