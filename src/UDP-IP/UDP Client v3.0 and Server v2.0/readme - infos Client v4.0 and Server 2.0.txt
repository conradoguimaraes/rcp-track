#------------------------------------------------------------------------
Version: 4.0

What it is: UDP Client

What it does: 
    1) Creates a Socket with certain parameters
    2) Reads XML File
    3) Encodes XML File
    4) Sends the Encoded XML Data to the Server (v2.0)
    5) Waits for the Server's Reply
    6)   repeat 2
#------------------------------------------------------------------------
Version: 2.0

What it is: UDP Server

What it does: 
    1) Creates a Socket with certain parameters
    2) Executes 3 parallel-independent threads:
        #Thread-1 - keeps listening at UDP assigned Port
        #Thread-2 - generate random STR and INT
        #Thread-3 - does something after x amount of time
#------------------------------------------------------------------------