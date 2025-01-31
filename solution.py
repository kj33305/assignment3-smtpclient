from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # mail_server = ("smtp.gmail.com", 587)
    # mail_server = ("smtp.mail.yahoo.com", 465)
    # mail_server = ("smtp.aol.com", 25)
    # mail_server = ("smtp.sendgrid.com", 587)
    # mail_server = ("mail.smtp2go.com", 2525)
    mail_server = ("127.0.0.1", 1025)
    # mail_server = ("smtp.test.com", 1025)
    # mail_server = ("mail.nyu.edu", 995)
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mail_server)
    #print("I created a socket.  Yay.")
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    messageFrom = "MAIL FROM: <kevinjohnson1999@yahoo.com>\r\n"
    clientSocket.send(messageFrom.encode())
    # print(messageFrom)
    recv2 = clientSocket.recv(1024)
    recv2 = recv2.decode()
    # print(recv2)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    recTo = "RCPT TO: <kevinjohnson1999@gmail.com>\r\n"
    clientSocket.send(recTo.encode())
    recv3 = clientSocket.recv(1024)
    recv3 = recv3.decode()
    # print(recv)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    recv4 = recv4.decode()
    # print("DATA sent")
    # print(recv4)
    # print("DATA receipt")
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "This is my test mail subject for programming assignment 3"
    # print(subject)
    clientSocket.send(subject.encode())
    clientSocket.send(msg.encode())
    #print("Sent encoded subject and message")
    #recv6 = clientSocket.recv(1024)# - Commented out because not expecting server response
    #recv6 = recv6.decode()# - Commented out because not expecting server response
    #print("Received response after subject and message sent")
    #print(recv6)
    ##clientSocket.send(msg.encode())
    # recv7 = clientSocket.recv(1024)
    # recv7 = recv7.decode()
    # print(recv7)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv8 = clientSocket.recv(1024)
    recv8 = recv8.decode()
    #print(recv8)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv9 = clientSocket.recv(1024)
    recv9 = recv9.decode()
    #print(recv9)
    # clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')