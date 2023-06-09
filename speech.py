# Author - Adekunle Adegbie
# The following code is given as part of my project and is to be used at your own risk
#
# The following are the dependencies
# pip3 install pydub
#
# Ensure you have the aws cli installed and configured with default region and access credentials
#
# Visit the below link for the different voiceId
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.synthesize_speech

import boto3
import json
import io
from pydub import AudioSegment
from pydub.playback import play

client = boto3.client('polly')

def playsound(speech, voice='Amy'):
	response = client.synthesize_speech(
		Text=speech,
		TextType='text',
		VoiceId=voice,
		OutputFormat='ogg_vorbis',
		SampleRate='8000',
	)

	print(response)
	audiostream = response['AudioStream'].read()
	audiosegment = AudioSegment.from_file(io.BytesIO(audiostream), format="ogg")
	play(audiosegment)


playsound('Hello customer, how can we service you better today?')
#playsound('Hello customer, how can we service you better today?', 'Aditi')
#playsound('Hello customer, how can we service you better today?', 'Brian')
#playsound('Hello customer, how can we service you better today?', 'Russell')
#playsound('Hello customer, how can we service you better today?', 'Salli')
#playsound('Hello customer, how can we service you better today?', 'Seoyeon')
#playsound('Hello customer, how can we service you better today?', 'Ravenna')
#playsound('Hello customer, how can we service you better today?', 'Tatyana')
#playsound('Hello customer, how can we service you better today?', 'Vitoria')
#playsound('Hello customer, how can we service you better today?', 'Zeina')
#playsound('Hello customer, how can we service you better today?', 'Zhiyu')

