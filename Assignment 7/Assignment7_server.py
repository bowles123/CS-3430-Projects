# Brian Bowles, Assignment 7, March 3, 2015.
import socket
import random
from math import exp

# Returns true if the given number is prime, false otherwise.
# num_trials defaulted to 50 because that seems to give me
# the most accurate answer.
def is_fermat_prime(num, num_trials = 50):
    if num == 1:
        return False
    
    trial, a = 1, random.randint(1, num - 1)

    while trial <= num_trials:
        if a**(num) % num == a % num and num % 2 != 0:
            return True;
        trial += 1
    return False;

# Finds all prime numbers in a give list.
def primes(num):
    primes, lst = [], generate_list(num)

    for i in range(len(lst)):
        if is_fermat_prime(lst[i])== True:
            primes.append(lst[i])
    return primes;

 # Generates a list of random numbers.   
def generate_list(number):
    list_ , current = [], 1

    while number + 1 != current:
        list_.append(current)
        current += 1
    return list_

## 1. construct a server socket object
server_socket = socket.socket()

## 2. get the hostname
host = socket.gethostname()
print 'host:', host
## 3. set the port number
port = 20005
print 'port:', port

## 4. bind the socket to the host
##    and the port
server_socket.bind((host, port))

## 5. specify the number of connections
##    that can be queued up on the
##    socket.
server_socket.listen(5)

## 6. go into infinite loop
while True:
    ## 6.1. accept connections
    client_socket, address = server_socket.accept()
    ## 6.2. print the address of the connection
    print 'Got connection from', address
    n = client_socket.recv(1024)
    ## 6.3. send a simple string
    client_socket.send(str(primes(int(n))))
    ## 6.4 close the connection
    client_socket.close()

    
