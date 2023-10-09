#------------------------------------------------------------------------
Version: 2.0

What it is: UDP Client

What it does: 
    1) Creates a Socket with certain parameters
    2) Sends a Message to the Server (v1.0)
    3) Waits for the Server's Reply
    4)  repeat n.ยบ 2
    
    OBS: The cycle ends after the Message #100

#------------------------------------------------------------------------
Version: 1.0

What it is: UDP Server

What it does: 
    1) Creates a Socket with certain parameters
    2) Keeps waiting for a Message sent by a Client
    3) Prints, to the terminal, the Client Messange and IP/Port
#------------------------------------------------------------------------