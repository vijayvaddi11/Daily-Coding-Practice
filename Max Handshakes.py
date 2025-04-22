# Q17. Finding Maximum Number Of Handshakes

num = int(input())
max_handshakes = int(((num-1)*num)/2)
print(f'Maximum number of handshakes possible for {num} people are : {max_handshakes}')