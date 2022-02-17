import os
import json
# from pprint import pprint

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    # {filename{text:(start end)}}
    def process(self, data, inputs, utils):
        # print('I am here')
        for yt in data:
            # print('No 2')
            if not utils.caption_file_exists(yt):
                continue
            for caption_file in os.listdir(CAPTIONS_DIR):
                # print(caption_file)
                with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                    captions = {}
                    for line in f:
                        # print(type(line))
                        # print(' No 1')
                        line = json.loads(line)                  # Use json.loads to make str --> dictionary format

                        # captions = {line['text'], line['start']}   # captions = {text: start_time}
                        end_time = int(line['start']) + int(line["duration"])
                        captions[line['text']] = line['start'], float(end_time)
                        # captions = {line['start'], line['text']}

                        # print('new_caption', captions)
                # data[caption_file] = captions

            yt.captions = captions
        # pprint(data)
        return data

