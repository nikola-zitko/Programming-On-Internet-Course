import socket
import re

def connect_to_server(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    return s

def get_source(host, page, s):
    CRLF = '\r\n'
    request = 'GET /' + page + ' HTTP/1.1'
    request += CRLF
    request += 'Host: ' + host + CRLF
    request += CRLF

    s.sendall(str.encode(request, 'cp852'))
    return s.recv(100000).decode()

def get_links(source):
    link_list = []
    beg = 0
    while True:    
        beg_link = source.find('a href="', beg)
        if beg_link == -1:
            return link_list
        end_link = source.find('"', beg_link + 8)
        link = source[beg_link + 8:end_link]
        beg = end_link + 1
        if link not in link_list:
            link_list.append(link)

def deeper(link_list):
    for i in link_list:
        beg = 0
        while True:  
            s = connect_to_server("www.watchthatpage.com", 80)
            source = get_source("www.watchthatpage.com", i, s)  
            beg_link = source.find('a href="', beg)
            if beg_link == -1:
                return link_list
            end_link = source.find('"', beg_link + 8)
            link = source[beg_link + 8:end_link]
            beg = end_link + 1
            if link not in link_list:
                link_list.append(link)

s = connect_to_server("www.watchthatpage.com", 80)
source = get_source("www.watchthatpage.com", "watchPages.jsp", s)
print (source)
link_list = get_links(source)
print(deeper(link_list))



