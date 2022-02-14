from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    #mail_server = ("smtp.gmail.com", 587)
    #mail_server = ("smtp.mail.yahoo.com", 465)
    #mail_server = ("smtp.aol.com", 25)
    #mail_server = ("smtp.sendgrid.com", 587)
    #mail_server = ("mail.smtp2go.com", 2525)
    mail_server = ("smtp.test.com", 1025)
    #mail_server = ("mail.nyu.edu", 995)
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mail_server)
    # Fill in end
    #print("Socket")
    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        #print('220 reply not received from server.')
    #print("Got a 220")

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        #print('250 reply not received from server.')
        #print(heloCommand)

    # Send MAIL FROM command and handle server response.
    # Fill in start

    global messageFrom
    messageFrom = "MAIL FROM: <kevinjohnson1999@yahoo.com>\r\n"
    clientSocket.send(messageFrom.encode())
    #print(messageFrom)
    recv2 = clientSocket.recv(1024)
    recv2 = recv2.decode()
    #print(recv2)
    # Fill in end
    #print('Hello')

    # Send RCPT TO command and handle server response.
    # Fill in start
    recTo = "RCPT TO: <kevinjohnson1999@gmail.com>\r\n"
    clientSocket.send(recTo.encode())
    recv3 = clientSocket.recv(1024)
    recv3 = recv3.decode()
    # Fill in end
    #print(recv3)

    # Send DATA command and handle server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    recv4 = recv4.decode()
    #print(recv4)
    #print("After4")
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "This is my test mail subject for programming assignment 3"
    clientSocket.send(subject.encode())
    #recv6 = clientSocket.recv(1024)
    #print(recv6)
    clientSocket.send(msg.encode())
    recv7 = clientSocket.recv(1024)
    #print(recv7)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv8 = clientSocket.recv(1024)
    # Fill in end
    #print(recv8)

    # Send QUIT command and handle server response.
    # Fill in start
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv9 = clientSocket.recv(1024)
    #print(recv9)
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')