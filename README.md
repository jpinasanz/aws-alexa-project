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
First, to get lecture audio from mediasite we set up a custom transcription provider in mediasite that will automatically send videos to our server when requested This was handled in the mediasite management portal. Our server is set up on AWS EC2 and is set up to recieve videos through .mp4. Once videos get to the server they are detected by SftpWatcher.py which starts a new Captioning.py thread that runs the transcription job. Once the .srt has been created we send the srt back to mediasite and dispose of all the temporary files.

3) How to setup
_______________________________________________________________________________
	For this project I have chosen to use AWS Python SDK, Boto 3. This is
	is because AWS has included a full API for AWS services within Boto 3
	and we can quickly make calls to many of the AWS functions in python.

	In order to use Boto 3, you must install it in your system.
	the files botoUploadfile and botoStartTranscriptionJob were created 
	loaded in Python3 and Boto 3. Refer to the AWS boto3 instructions on
	how to install.[Boto 3 Install Instructions](https://www.boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
	
	In order to access the files within the ITS AWS Account you need to create
	a user within the AWS IAM service. To do this, log into AWS and go to IAM,
	on the left hand side click on 'Users' and create a new user. 
	Fill in your name (i.e. John Doe would jdoe), 
	enable 'Programmatic Access' and 'AWS Management Console access' 
	you can choose to autogenerate a password or create a new one and disable
       	and disable 'Require password reset.'Click 'Next:Permissions' and on this
       	page click the box next the line 'itsstudentassitants', click 'Next', make
       	no tags and click 'Next' review the informatoin and click 'Create user'. 
	
	This last step is important. On the final page there will be a line with
       	your new user information. This line will include your username,
       	Access key ID (SAVE THIS), Secret access key (SAVE THIS) and
       	Password (SAVE THIS TOO). The Access key ID and Secret access key are
       	both required to provide you with access to AWS through the 
	AWS Command Line Interface (CLI).

	Now you may be asking, what is AWS CLI? CLI is how we communicate with AWS
       	and how we authenticate your access to the ITS AWS programs and resources.
	In order to access this we need to install AWS CLI, this can be done by 
	following the steps provided in the AWS CLI install page.
	[AWS CLI Install](docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

	If you're on Windows download the installer, the installer will walk you through
	the steps on getting CLI on your computer.
	If you're on Linux or macOS, follow the link for installation on Linux or macOS.
	The Amazon page will guide you on how to install CLI through terminal. 	

	Now that you have CLI installed in your system, its time to configure CLI
	so that you can call functions from Boto 3 and access our files in S3. 

	Hopefully by this point you are familiar with terminal in macOS or you have
       	Ubuntu or some kind of linux distro installed in Windows so you have access
       	to a terminal.
	
	In terminal you're gonna want to type in:
	aws configure

	This will bring in prompts to fill in your AWS Access Key ID and
       	other information from the IAM step. Fill in your information as follows:

	AWS Access Key ID: <your access key>
	AWS Secret Access Key: <your sercret access key>
	Default region name: us-west-2
	Default output format: json

	By this point you should be good to go. You've installed Boto 3 so you have
	access to the AWS SDK, you've set yourself up a new user with appropriate
	keys for access and you've installed AWS CLI and configured it so it will
	recognize your authentication and grant you access to the ITS AWS S3.


