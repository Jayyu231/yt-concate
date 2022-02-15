import os
import json
from pprint import pprint

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        # os.listdir(utils.get_video_list_filepath(url))
        # print('path', CAPTIONS_DIR)
        # os.listdir(CAPTIONS_DIR)
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            # print(caption_file)
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                captions = {}
                for line in f:
                    # print(type(line))
                    res = json.loads(line)                  # Use json.loads to make str --> dictionary format
                    # print('caption_file'+'res', caption_file, '+', res)
                    # print(type(res))
                    # print(res['text'])
                    # captions = {res['text'], res['start']}   # captions = {text: start_time}
                    end_time = int(res['start']) + int(res["duration"])
                    captions[res['text']] = res['start'], float(end_time)
                    # captions = {res['start'], res['text']}

                    # print('new_caption', captions)
            data[caption_file] = captions
        pprint(data)
        return data

