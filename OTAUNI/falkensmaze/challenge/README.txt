Challenge Title: Falken's Maze
Category: Forensics/Crypto
Description: You have stumbled upon one of NORADS computer systems but are unable to login. ssh falken@servernameandport
File To Host: swpag.jpg
Point Value: 300
OTA{a_strange_game}

Docker file spins up Debian Container running open ssh. SSH has been locked down to need private key. The file include 
'authorized_keys', and 'flag' need to be in the same directory as the Dockerfile when running docker build.
For the challenge Description I want to host the swpag.jpg file and to ssh falken@server
