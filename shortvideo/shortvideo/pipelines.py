# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from shortvideo.items import Shortvideo

logger = logging.getLogger(__name__)


class ShortvideoPipeline(object):
    def process_item(self, item, spider):
        try:
            video = Shortvideo.get(Shortvideo.platform == item['platform'], Shortvideo.uuid == item['uuid'])
            telta = self.telta_sec(video.updated_at)
            if telta >= 86400 :
                video.title = item['title']
                video.width = item['width']
                video.height = item['height']
                video.duration = item['duration']
                video.thumbnail_uri = item['thumbnail_uri']
                video.video_uri = item['video_uri']
                video.share_uri = item['share_uri']
                video.preview_uri = item['preview_uri']
                video.liked_num = item['liked_num']
                video.loop_num = item['loop_num']
                video.view_num = item['view_num']
                video.comment_num = item['comment_num']
                video.share_num = item['share_num']
                video.avg_view_time = item['avg_view_time']

                video.user_id = item['user_id']
                video.user_nick_name = item['user_nick_name']
                video.user_real_name = item['user_real_name']
                video.user_display_name = item['user_display_name']
                video.user_desc = item['user_desc']
                video.user_icon = item['user_icon']
                video.updated_at = datetime.now()
                video.save()
        except Shortvideo.DoesNotExist:
            Shortvideo.create(
                platform = item['platform'],
                uuid = item['uuid'],
                title = item['title'],
                width = item['width'],
                height = item['height'],
                duration = item['duration'],
                thumbnail_uri = item['thumbnail_uri'],
                video_uri = item['video_uri'],
                share_uri = item['share_uri'],
                preview_uri = item['preview_uri'],
                liked_num = item['liked_num'],
                loop_num = item['loop_num'],
                view_num = item['view_num'],
                comment_num = item['comment_num'],
                share_num = item['share_num'],
                avg_view_time = item['avg_view_time'],

                user_id = item['user_id'],
                user_nick_name = item['user_nick_name'],
                user_real_name = item['user_real_name'],
                user_display_name = item['user_display_name'],
                user_desc = item['user_desc'],
                user_icon = item['user_icon'],
                created_at = datetime.now(),
                updated_at = datetime.now()
            )
        return item

    def telta_sec(self, source):
        if source is None:
            return 86401
        now = datetime.now()
        telta = now - source
        return int(telta.total_seconds())
