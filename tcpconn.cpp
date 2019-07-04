/*
static void handleClient(int sock) {
    char buffer[BTYES];
    char request[BYTES];
    memset((void*) request, (int) '\0', BYTES);
    int rcvd = read(sock, request, BYTES);

    if (rcvd < 0)
        perror("socket receive");
    else if (rcvd == 0)
        perror("client disconnected without reason");
    else
        httpRequest(sock, request);

    shutdown(sock, SHUT_RDWR);
    close(sock);
*/
