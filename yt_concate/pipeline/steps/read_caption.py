import os
import json
from pprint import pprint

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    # {filename{text:(start end)}}
    def process(self, data, inputs, utils):

        for yt in data:

            if not utils.caption_file_exists(yt):
                continue
            # for caption_file in os.listdir(CAPTIONS_DIR):

                # with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
            captions = {}
            with open(yt.caption_filepath, 'r') as f:

                for line in f:

                    line = json.loads(line)                  # Use json.loads to make str --> dictionary format

                    # captions = {line['text'], line['start']}   # captions = {text: start_time}
                    end_time = int(line['start']) + int(line["duration"])
                    captions[line['text']] = line['start'], end_time
                    # captions = {line['start'], line['text']}

                    # print('new_caption', captions)
                # data[caption_file] = captions

            yt.captions = captions
            # pprint(data)
        return data

