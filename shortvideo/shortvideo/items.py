# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from peewee import *
from datetime import datetime

db = MySQLDatabase("shortvideo", host='127.0.0.1', port=3306, user='root',
                   passwd='fff123456', charset='utf8mb4')

class ShortvideoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    platform = scrapy.Field()
    uuid = scrapy.Field()
    title = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    duration = scrapy.Field()
    thumbnail_uri = scrapy.Field()
    video_uri = scrapy.Field()
    share_uri = scrapy.Field()
    preview_uri = scrapy.Field()
    liked_num = scrapy.Field()
    loop_num = scrapy.Field()
    view_num = scrapy.Field()
    comment_num = scrapy.Field()
    share_num = scrapy.Field()
    avg_view_time = scrapy.Field()
    user_id = scrapy.Field()
    user_nick_name = scrapy.Field()
    user_real_name = scrapy.Field()
    user_display_name = scrapy.Field()
    user_icon = scrapy.Field()
    user_desc = scrapy.Field()


class Shortvideo(Model):
    id = IntegerField(verbose_name="id", primary_key=True, null=False)
    platform = SmallIntegerField(verbose_name="platform", null=False)
    uuid = CharField(verbose_name="uuid", null=False)
    title = CharField(verbose_name="title", null = True)
    width = SmallIntegerField(verbose_name="width", null = True)
    height = SmallIntegerField(verbose_name="height", null = True)
    duration = SmallIntegerField(verbose_name="duration", null = True)
    thumbnail_uri = CharField(verbose_name="thumbnail_uri", null = True)
    video_uri = CharField(verbose_name="video_uri", null = True)
    share_uri = CharField(verbose_name="share_uri", null = True)
    preview_uri = CharField(verbose_name="preview_uri", null = True)

    liked_num = SmallIntegerField(verbose_name="liked_num", null = True)
    loop_num = SmallIntegerField(verbose_name="loop_num", null = True)
    view_num = SmallIntegerField(verbose_name="view_num", null = True)
    comment_num = SmallIntegerField(verbose_name="comment_num", null = True)
    share_num = SmallIntegerField(verbose_name="share_num", null = True)
    avg_view_time = SmallIntegerField(verbose_name="avg_view_time", null = True)

    user_id = CharField(verbose_name="user_id", null = True)
    user_nick_name = CharField(verbose_name="user_nick_name", null = True)
    user_real_name = CharField(verbose_name="user_real_name", null = True)
    user_display_name = CharField(verbose_name="user_display_name", null = True)
    user_desc = CharField(verbose_name="user_desc", null = True)
    user_icon = CharField(verbose_name="user_icon", null = True)
    created_at = DateTimeField(default=datetime.now(), null=True)
    updated_at = DateTimeField(default=datetime.now(), null=True)


    class Meta:
        database = db
        table_name = 'short_video'
