# MAT: Malware Analysis Tool

Sends requests to suspected malware hosts and logs the response for further 
analysis. 

## How to Test

1. Clone this repo `git clone https://github.com/shakabra/MAT.git`
2. Navigate to the `mat` directory and `python main.py` this will:
  - create a log directory with timestamped log files
  - print the list of user agent from ualist.txt


## Next Steps...
Help make MAT do things:
  - Check out the the user agent file and add more user agents. Some malicious
  hosts will respond differently to different hosts. MAT will record a log for
  each user agent so they can be diffed to identify the rules on the target.
  - Come up with interesting stuff for MAT to do.
