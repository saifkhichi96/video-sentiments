import os

from moviepy.editor import *


def vid2audio(infile, outdir='.') -> str :
    """Converts a video to a waveform audio.

    The audio file is saved in the specified folder, with same filename as the
    input file, but .wave extension.

    Parameters:
        infile (str) : Full path of the video file to convert.
        outdir (str) : Path of the folder where to save the output. Default is
                       current directory.

    Returns:
        Location of the saved audio file on success.

    Throws:
        A general exception would be raised if there is any kind of error.
    """
    input = VideoFileClip(infile)
    audio = input.audio

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    fn = os.path.splitext(os.path.split(infile)[-1])[0]
    audio.write_audiofile(os.path.join(outdir, f'{fn}.wav'))
    return str(os.path.join(outdir, f'{fn}.wav'))
