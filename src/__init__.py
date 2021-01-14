from .sentiments import analyze_sentiment_google
from .transcribe import transcribe
from .vid2audio import vid2audio


def analyze_sentiment(video_file, verbose=False):
    import os
    tmpdir = os.path.split(video_file)[0]

    if verbose:
        print(f'Converting {video_file} to a waveform audio...')

    try:
        audio_file = vid2audio(video_file, tmpdir)
        if verbose:
            print('Transcribing the audio with Google Speech-to-Text engine...')
        transcript = transcribe(audio_file)

        sentiments = []
        combined_text = ''
        for text in transcript:
            combined_text += f'{text} '
            score = analyze_sentiment_google(text)
            sentiments.append((text, score))
            if verbose:
                print(f'{text}: {score}')

        score = analyze_sentiment_google(combined_text)
        if verbose:
            print(f'{text}: {score}')

        sentiments.append((combined_text, score))
        return sentiments
    except Exception as ex:
        if verbose:
            print(str(ex))
            print('Terminating operation!')
        raise ex
