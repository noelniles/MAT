# MAT: Malware Analysis Tool

Sends requests to suspected malware hosts and logs the response for further 
analysis. 

## How it Works

### Targets
**MAT** sends requests to web servers using cURL. The list of sites can be 
found in `mat/targets/badfile.txt`. You can add any more URLs to the list; one
URL per line. The URLs should be servers that respond to port 80, because **MAT**
just uses HTTP right now. The idea is to find targets that respond with
malicious code.

### Requests
**MAT** builds custom https headers and pretends to be a normal web browser.
The default user agent is IE7 Windows XP, but it can be changed in `mat/conf/matconf.py`.

### Logging
**MAT** logs the response from the target in a file called
`mat/logs/<target_name>/<scan_time>_response.log`. There is also a function
to make a separate log for cookies that the targets send back, but it's not
implemented yet.

### Analysis
**MAT** will parse through the logged responses and identify suspicious files.
It will also follow links and try to build relationships between malicious hosts.
*of course nothing in this section is implemented yet, but it sounds good.*

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
