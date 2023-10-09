%%
% UDP Client Code in MATLAB

% Define the remote server's IP address and port number
serverIP = '127.0.0.1'; % Replace with the IP of your UDP server
serverPort = 12345;    % Replace with the port number your UDP server is listening on

% Create a UDP socket object
udpClient = udp(serverIP, serverPort);

% Set the communication timeout (optional)
set(udpClient, 'Timeout', 5);

% Open the UDP socket for communication
fopen(udpClient);

% Define the message to be sent
message = 'Hello, UDP Server!';

% Convert the message to a byte array
messageData = uint8(message);

% Send the message to the server
fwrite(udpClient, messageData);

% Receive a response from the server (optional)
% You can use fread() or fscanf() to receive data from the server if needed.

% Close the UDP socket when done
fclose(udpClient);

% Clean up
delete(udpClient);
clear udpClient;
