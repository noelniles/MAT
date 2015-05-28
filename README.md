# MAT: Malware Analysis Tool

Sends requests to suspected malware hosts and logs the response for further 
analysis. 

## How to Test

1. Clone this repo `git clone https://github.com/shakabra/MAT.git`
2. Navigate to the `mat/src` directory and run `python mat.py -t all` this will:
  - run all tests in the tests directory
  - create an example log file
3. Running `python mat.py` with no arguments should make requests to all the
   sites in _badfile.txt_ and log the responses in _logs/_.
4. More tests can be added by putting a module in _tests/_ called
   `<MODNAME>_test.py` and adding a argument to _mat.py_. All tests should 
   return True on success.
5. IP addresses can be added or removed from _badfile.txt_; one address per
   line. See **Next Steps** for info on making this better.

## Next Steps...
### Help make MAT do things:
  - Make a parser for the log files and pick out interesting things.
  - Add functionality to grab bad URLs from the Internet and update 
    _badfile.txt_ by running something like `mat.py -u badfile`.
  - Check out the the user agent file and add more user agents. Some malicious
  hosts will respond differently to different hosts. MAT will record a log for
  each user agent so they can be diffed to identify the rules on the target.
  - Experiment with changing the referer found in _request.py_.
  - Come up with interesting stuff for MAT to do.
