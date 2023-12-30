#include <iostream>
#include <cstring>
#include <unistd.h>
#include <sys/socket.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/rfcomm.h>


// g++ -o your_program_name your_program_name.cpp -lbluetooth
int main() {
    const char* bd_addr = "78:C3:E9:06:A2:F1";
    struct sockaddr_rc addr = { 0 };
    int s, status;

    // allocate a socket
    s = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM);

    // set the connection parameters (BD_ADDR and channel)
    addr.rc_family = AF_BLUETOOTH;
    addr.rc_channel = (uint8_t) 1; // Assuming channel 1, change if needed
    str2ba(bd_addr, &addr.rc_bdaddr);

    // connect to the remote device
    status = connect(s, (struct sockaddr*)&addr, sizeof(addr));

    // check for errors
    if (status < 0) {
        perror("Connection failed");
        close(s);
        return 1;
    }

    // connection successful, you can now use 's' to communicate with the device

    // for example, send some data
    const char* message = "Hello, Bluetooth!";
    status = write(s, message, strlen(message));

    // check for errors
    if (status < 0) {
        perror("Write failed");
    }

    // close the socket when done
    close(s);

    return 0;
}
