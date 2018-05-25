import scrapy
import json
import logging
from shortvideo.items import ShortvideoItem

logger = logging.getLogger(__name__)


class MusicallySpider(scrapy.Spider):
    name = "musically"

    def __init__(self, *args, **kwargs):
        self.domain = "https://api.musical.ly"
        self.headers = {
            'X-Request-Info5':
            'eyJvc3R5cGUiOiJpb3MiLCJvcyI6ImlPUyAxMS4zIiwiWC1SZXF1ZXN0LUlEIjoiMDM2QzBCQ0ItMTcwNC00RjczLTlGM0QtMjMxODM5ODc3MDI4Iiwic2xpZGVyLXNob3ctY29va2llIjoiVlVsRVh6RkRORVExUXpJNVJrSTNPVUl4TlVZNE5ETkVOVUU1TlRNNVJrVTJSakF4WDNGeFgzVnVhVzl1T2tWU2NrMU1ZVVZ6ZURCdmJtNTNSM0Z3Y0V0c01VRTlQVHBqWkdVeU1HSTVNek5qWkdabVpURTBZekJrTXpsaFlUTmtPREptWTJNMU9UbzJOVFF6TVRVMk1UTTJNakUwTnprMU1qYzUiLCJtZXRob2QiOiJHRVQiLCJkZXZpY2VpZCI6ImkwMzlkM2JlYTIxNzEzNGE5OGIyMWIyOTg2ZDc0NDhiOGQ2NSIsInZlcnNpb24iOiI2LjguMiIsInRpbWVzdGFtcCI6IjE1MjM0NDc5NzkwMDAiLCJ1cmwiOiJodHRwczpcL1wvYXBpLm11c2ljYWwubHlcL3Jlc3RcL211c2ljYWxzXC9leHBsb3JlXC9saXN0P2xpbWl0PTgmX19fZD1leUpoWXlJNklreEpVMVFpTENKaWVpSTZJbVY0Y0d4dmNtVmZaR2x6WTI5MlpYSjVJaXdpWkcwaU9pSk5WVk5KUTBGTUlpd2lkbVZ5SWpvaVpHVm1ZWFZzZENKOSZob3RLZXk9bW9kZWwmZGlzcGxheU1vZGU9MSJ9',
            'build': '20180322001',
            'slider-show-cookie':
            'VUlEXzFDNEQ1QzI5RkI3OUIxNUY4NDNENUE5NTM5RkU2RjAxX3FxX3VuaW9uOkVSck1MYUVzeDBvbm53R3FwcEtsMUE9PTpjZGUyMGI5MzNjZGZmZTE0YzBkMzlhYTNkODJmY2M1OTo2NTQzMTU2MTM2MjE0Nzk1Mjc5',
            'X-Request-Sign5': '01i6fdda67ba8996880438054fb1dad7d6257f9298a6'
        }
        super().__init__(*args, **kwargs)

    def start_requests(self):
        urls = [
            '/rest/musicals/explore/list?limit=10&___d=eyJhYyI6IkxJU1QiLCJieiI6ImV4cGxvcmVfZGlzY292ZXJ5IiwiZG0iOiJNVVNJQ0FMIiwidmVyIjoiZGVmYXVsdCJ9&hotKey=model&displayMode=1',
        ]
        for url in urls:
            yield scrapy.Request(url=self.domain+url, headers=self.headers,
                callback=self.parse, dont_filter=True)

    def parse(self, response):
        retval = json.loads(response.body)
        items, next = self.extract_video(retval)
        for item in items:
            logger.info("Get Platform: %s, uuid : %s", item['platform'], item['uuid'])
            yield item
        if next is not None:
            yield scrapy.Request(url=self.domain+next, headers=self.headers,
                callback=self.parse, dont_filter=True)

    def extract_video(self, data):
        success = data['success']
        results = data['result']
        if not success:
            return None, None
        ret_list = results['list']
        retvals = []
        for item in ret_list:
            #video = ShortvideoItem(uuid=item['musicalId'])
            video = self.build_item(item)
            retvals.append(video)
            # logger.info (item['musicalId'])

        next = results['next']
        if not next:
            return retvals, None

        return retvals, next['url']

    def build_item(self, data):
        #logger.error(data)
        if data is None or data['musicalId'] is None:
            return None
        video = ShortvideoItem(
            uuid = data['musicalId'],
            platform = 1
        )
        if 'caption' in data:
            video['title'] = data['caption']
        else:
            video['title'] = ''
        if 'width' in data:
            video['width'] = data['width']
        else:
            video['width'] = 0
        if 'height' in data:
            video['height'] = data['height']
        else:
            video['height'] = 0
        if 'duration' in data:
            video['duration'] = data['duration']
        else:
            video['duration'] = 0
        if 'thumbnailUri' in data:
            video['thumbnail_uri'] = data['thumbnailUri']
        else:
            video['thumbnail_uri'] = ''
        if 'videoUri' in data:
            video['video_uri'] = data['videoUri']
        else:
            video['video_uri'] = ''
        if 'shareUri' in data:
            video['share_uri'] = data['shareUri']
        else:
            video['share_uri'] = ''
        if 'previewUri' in data:
            video['preview_uri'] = data['previewUri']
        else:
            video['preview_uri'] = ''
        if 'likedNum' in data:
            video['liked_num'] = data['likedNum']
        else:
            video['liked_num'] = 0
        if 'loopNum' in data:
            video['loop_num'] = data['loopNum']
        else:
            video['loop_num'] = 0
        if 'completeViewNum' in data:
            video['view_num'] = data['completeViewNum']
        else:
            video['view_num'] = 0
        if 'commentNum' in data:
            video['comment_num'] = data['commentNum']
        else:
            video['comment_num'] = 0
        if 'shareNum' in data:
            video['share_num'] = data['shareNum']
        else:
            video['share_num'] = 0
        if 'avgViewTime' in data:
            video['avg_view_time'] = data['avgViewTime']
        else:
            video['avg_view_time'] = 0

        if 'author' in data:
            if 'userId' in data['author']:
                video['user_id'] = data['author']['userId']
            else:
                video['user_id'] = ''
            if 'nickName' in data['author']:
                video['user_nick_name'] = data['author']['nickName']
            else:
                video['user_nick_name'] = ''
            if 'realName' in data['author']:
                video['user_real_name'] = data['author']['realName']
            else:
                video['user_real_name'] = ''
            if 'displayName' in data['author']:
                video['user_display_name'] = data['author']['displayName']
            else:
                video['user_display_name'] = ''
            if 'userDesc' in data['author']:
                video['user_desc'] = data['author']['userDesc']
            else:
                video['user_desc'] = ''
            if 'icon' in data['author']:
                video['user_icon'] = data['author']['icon']
            else:
                video['user_icon'] = ''
        else:
            video['user_id'] = ''
            video['user_nick_name'] = ''
            video['user_real_name'] = ''
            video['user_display_name'] = ''
            video['user_desc'] = ''
            video['user_icon'] = ''
        return video
