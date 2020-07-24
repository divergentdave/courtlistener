# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-22 23:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favorites', '0004_add_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text=b'The time when this item was created')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text=b'The last moment when the item was modified.')),
                ('object_id', models.PositiveIntegerField()),
                ('name', models.SlugField(help_text=b'The name of the tag')),
                ('title', models.TextField(blank=True, help_text=b'A title for the tag')),
                ('description', models.TextField(blank=True, help_text=b'The description of the tag in Markdown format')),
                ('view_count', models.IntegerField(db_index=True, default=0, help_text=b'The number of times the URL for the tag has been seen.')),
                ('published', models.BooleanField(db_index=True, default=False, help_text=b'Whether the tag has been shared publicly.')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(help_text=b'The user that created the tag', on_delete=django.db.models.deletion.CASCADE, related_name='user_tags', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterIndexTogether(
            name='usertag',
            index_together=set([('user', 'name')]),
        ),
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('date_created',
                 models.DateTimeField(auto_now_add=True, db_index=True,
                                      help_text=b'The time when this item was created')),
                ('status', models.SmallIntegerField(
                    choices=[(1, b'Still waiting for the document.'),
                             (2, b'Prayer has been granted.')], default=1,
                    help_text=b'Whether the prayer has been granted or is still waiting.')),
                ('recap_document', models.ForeignKey(
                    help_text=b"The document you're praying for.",
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='prayers', to='search.RECAPDocument')),
                ('user',
                 models.ForeignKey(help_text=b'The user that made the prayer',
                                   on_delete=django.db.models.deletion.CASCADE,
                                   related_name='prayers',
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterIndexTogether(
            name='prayer',
            index_together=set(
                [('recap_document', 'user'), ('recap_document', 'status'),
                 ('date_created', 'user', 'status')]),
        ),
    ]