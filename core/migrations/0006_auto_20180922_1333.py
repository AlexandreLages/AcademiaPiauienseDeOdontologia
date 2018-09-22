# Generated by Django 2.0.8 on 2018-09-22 16:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_cadeira_curso_diretoria_membro_sobre'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='modificado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='modificado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sobre',
            name='titulo',
            field=models.CharField(default=None, max_length=1000),
            preserve_default=False,
        ),
    ]
