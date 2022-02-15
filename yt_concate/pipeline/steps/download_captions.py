# standard library imports
import os
import json
import time

# related third party imports
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# local application/library specific imports
from .step import Step
from .step import StepException
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR


class DownloadCaptions(Step):  # 1. 繼承 Step 抽象類別
    def process(self, data, inputs, utils):  # 2. 覆寫 抽象方法
        start = time.time()
        # 我寫的：優先讀取以下載的連結檔案 video_url.txt
        yt_urls = open(os.path.join(VIDEOS_DIR, 'video_url.txt'), 'r', encoding='utf-8')

        # for url in data:
        for url in yt_urls:

            # print(url, end='')
            # print(utils.caption_file_exists(url))

            if utils.caption_file_exists(url):
                print('found existing caption file')
                continue

            video_id = url.split('watch?v=')[-1]
            # print(video_id, end='')

            try:
                captions = YouTubeTranscriptApi.get_transcript(video_id)
                captions_l = list(json.dumps(i) for i in captions)

                with open(os.path.join(CAPTIONS_DIR, video_id.replace("\n", "") + ".txt"), "w", encoding='UTF-8') as fp:
                    for i in captions_l:
                        fp.write(i + '\n')

            except Exception:
                pass                            # 如果這個英文字幕檔無法下載，就跳過他，繼續下載其他的。
                # continue
                # raise StepException
        #
        yt_urls.close()
        end = time.time()
        print('took', end - start, 'seconds')
