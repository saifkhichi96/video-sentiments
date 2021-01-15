import io

# from google.cloud import speech
from google.cloud import speech_v1p1beta1 as speech


def transcribe(speech_file):
    """Transcribe the given audio file."""
    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    metadata = speech.RecognitionMetadata()
    metadata.recording_device_type = (
        speech.RecognitionMetadata.RecordingDeviceType.SMARTPHONE
    )
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        audio_channel_count=2,
        enable_automatic_punctuation=True,
        enable_speaker_diarization=True,
        diarization_speaker_count=2,
        use_enhanced=True,
        model="video",
        metadata=metadata,
    )

    response = client.recognize(config=config, audio=audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    transcript = []
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        transcript.append(result.alternatives[0].transcript.strip())

    return transcript
