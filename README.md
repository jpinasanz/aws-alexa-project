READ_ME 

1) Introduction
2) How we're doing it
3) How to setup 

_______________________________________________________________________________
1) Introduction
_______________________________________________________________________________
	This the the READ_ME for the ITS Amazon Transcribe project!
	This project is aimed at using Amazon Webservices (AWS) to 
	create transcriptions of recorded lecture audio so we can make
	accurate subtitles that our students can use!

2) How we're doing it
_______________________________________________________________________________
	There are a couple of steps involved in converting the lecture
	audio from Mediasite to AWS then back to us. We've outlined
	the process in a couple of steps (very subject to change).
	
	The first step is to access the stored audiofiles from Mediasite.
	Currently these are stored locally, talk to Kao on how to access
	these files and how to use them.

	Next, once we have access to these files we will upload them to the
	AWS S3. AWS will only work for us if have files stored in the S3.
	
	Next, we will make calls to the AWS Transcribe system to load our S3
	stored audio files and return a JSON format transcription file to a
	specified location in the S3.

	Once we have the transcription file, we can pull it from the S3 and 
	begin the process of converting it into a .srt file. The .srt is a
	commonly used file type in video subtitles. We have do not currently
	have a program for running this process.

	Finally, we verify that the correct video, audio, and subtitle files
	are in the proper location so blackboard can load them.

3) How to setup
_______________________________________________________________________________
	For this project I have chosen to use AWS Python SDK, Boto 3. This is
	is because AWS has included a full API for AWS services within Boto 3
	and we can quickly make calls to many of the AWS functions in python.

	In order to use Boto 3, you must install it in your system.
	the files botoUploadfile and botoStartTranscriptionJob were created 
	loaded in Python3 and Boto 3. Refer to the AWS boto3 instructions on
	how to install. 
	[Boto 3 Install Instructions](https://www.boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
