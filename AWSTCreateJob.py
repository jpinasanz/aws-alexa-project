from subprocess import call
from datetime import datetime
now = datetime.now()
timestamp=now.strftime("%m-%d-%Y_%H.%M.%S")

call(["aws", "transcribe", "start-transcription-job", "--transcription-job-name", timestamp, "--language-code", "en-US", "--media", "MediaFileUri=s3://its-demo-bucket/transcribe-sample.mp3", "--output-bucket-name", "its-demo-bucket" ])

