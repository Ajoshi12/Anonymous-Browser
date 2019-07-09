#include	<sys/socket.h>
#include	<arpa/inet.h>
#include	<errno.h>
#include	<stdio.h>
#include	<stdlib.h>
#include	<string.h>
#include    <unistd.h>
#include    <fcntl.h>


char                *ipaddress, *skeletonkey, *username, *dictionary, *password;

int	                sockfd;

char                skeletonKeyToBeCopied[400], responseFromClient[400];


struct sockaddr_in servaddr, cli_addr;
struct timeval tv; // timeout period for the server

static int scanport(int port)

{

	char buffer[256] = {0};
	int clilen = 0;
	int newsockfd = 0;

	int false = 0;
	//int true = 1;
	int found = false;
	int n;
	bzero((char*) &servaddr,sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	//servaddr.sin_addr.s_addr = hton1(INADDR_ANY);
	//servaddr.sin_port = htons(SERV_TCP_PORT);

    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        //perror("socket error");
		perror("client: can't open stream socket");
        exit(1);
    }

	tv.tv_sec = 1;
	tv.tv_usec = 0;

	// attempting to bind to server
     servaddr.sin_port = htons(port);
     if (bind(sockfd, (struct sockaddr *) &servaddr, sizeof(servaddr)) < 0)
	 {
              perror("ERROR on binding");
	 }

     listen(sockfd,5);
     clilen = sizeof(cli_addr);
     newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
     if (newsockfd < 0)
	 {
          perror("ERROR on accept");
	 }
     bzero(buffer,256);
     n = read(newsockfd,buffer,255);
     if (n < 0)
	 {
		 perror("ERROR reading from socket");
	 }
     printf("Here is the message: %s\n",buffer);
     n = write(newsockfd,"I got your message",18);
     if (n < 0)
	 {
		 perror("ERROR writing to socket");
	 }
    // return 0;



	 if (connect(sockfd, (struct sockaddr *) &servaddr, sizeof(servaddr)) != 0)
	 {
		 // do nothing
	 }

	// attempt to connect to the server
    if (connect(sockfd, (struct sockaddr *) &servaddr, sizeof(servaddr)) == 0)  // connection is all set and ready to go
	{
        printf("Port %d is open and ready to go.\n", port);

        if (write(sockfd, skeletonkey, strlen(skeletonkey)) < 0)
		{
            perror("Unable to write");
            exit(0);
        }
		else if (write(sockfd, skeletonkey, strlen(skeletonkey)) > 0)
		{
		// do nothing
		}

        bzero(responseFromClient, sizeof(responseFromClient));

		 if (recv > 0 && strstr(responseFromClient, "Username") != NULL)
		 {
            if (write(sockfd, username, strlen(username)) < 0)
			{
                perror("Unable to write");
                exit(0);
            }

            bzero(responseFromClient, sizeof(responseFromClient));
            if (read(sockfd, responseFromClient, 400) < 0)
			{
                perror("Unable to read");
                exit(0);
            }

            if (strstr(responseFromClient, "Password") != NULL)
			{
                printf("Port %d belongs to this user \"%s\".\n", port, username);
                printf("%s\n", "We will be entering dotted lines to seperate your output ----------------------");
                found = 1;
            }
        }
    }

    close(sockfd);
    return found;

}
// buffer overflow attack 

void bufferOverflow()
{
	char url[400];
	char bytes_recieved = {0};
	char connected[400];

    char *found;
	char *response;
    if ((found = strstr(response, "URL")) != NULL) {
        // get to the beginning of the actual url
        if (found != '\'')
		{
			perror("Have not been able to ffind start of the url");
		}
		else if (found == '\'')
		{
			perror("Have been able to find start of the url");
		}

	   char recv_data[bytes_recieved];

	char bytes_recieved = recv(connected, recv_data, 1024 - 1, 0);
    }

    printf("%s\n", url);
}


static int findport() // runs through every single port
{
    for (int i = 1024; i < 65536; i++)
	{
        if (scanport(i))
		{
            return i;
        }
    }

    return -1;
}


int main(int argc, char **argv)
{
    char *parametersToPort = "Parameters: findbackdoor <ipaddress> <skeleton key> <username> <dictionary>";

    if (argc != 5)
	{
        printf("%s\n", parametersToPort);
        exit(-1);
    }

    ipaddress = argv[1];
    skeletonkey = argv[2];
    username = argv[3];

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;



    if (inet_pton(AF_INET, ipaddress, &servaddr.sin_addr) > 0)
	{
       // do nothing
    }

    else if (inet_pton(AF_INET, ipaddress, &servaddr.sin_addr) <= 0)
	{
        printf("inet_pton error for %s", argv[1]);
        exit(0);
    }

    int port = 0;

	 if ((port = findport()) == -1)
	{
        // do nothing
    }
    else if ((port = findport()) != -1)
	{
        servaddr.sin_port = htons(port);
    }
	else
	{
        printf("Port for whatever reason is unable to be found. \n");
        exit(0);
    }

    return 0;
}