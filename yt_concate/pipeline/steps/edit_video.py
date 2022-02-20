from yt_concate.pipeline.steps.step import Step
from moviepy.editor import VideoFileClip, concatenate_videoclips


class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            print(found.yt.video_filepath)
            print(found.time)
            print(self.parse_caption(found.time))
            start, end = self.parse_caption(found.time)
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break
        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(output_filepath)

    def parse_caption(self, caption_time):
        start_sec, end_sec = caption_time
        return start_sec, end_sec
