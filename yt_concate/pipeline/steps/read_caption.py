import json
from pprint import pprint

from yt_concate.pipeline.steps.step import Step


class ReadCaption(Step):
    # {filename{text:(start end)}}
    def process(self, data, inputs, utils):

        for yt in data:

            if not utils.caption_file_exists(yt):
                continue
            captions = {}
            with open(yt.caption_filepath, 'r') as f:
                for line in f:
                    line = json.loads(line)                  # Use json.loads to make str --> dictionary format

                    # captions = {line['text'], line['start']}   # captions = {text: start_time}
                    end_time = int(line['start']) + int(line["duration"])
                    captions[line['text']] = line['start'], end_time

            yt.captions = captions
            # pprint(data)
            # print(captions)
        return data

