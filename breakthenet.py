import discord
import ipaddress
import socket
import requests
import json
import os

client = discord.Client()




def GetServiceName(port,protocol):
    serviceName = socket.getservbyport(port, protocol)
    return serviceName

def scanner(ip):
    for port in range(79, 82):
        print("Port: " + str(port))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        ports = []
        # returns an error indicator
        result = s.connect_ex((ip, port))
        if result == 0:
            ports.append(port)
            print("Port {} is open".format(port))
        return ports


def GetWebContent(url):
    r = requests.get(url)
    reply = "```" + r.text + "```"
    return reply

def port_scan(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = s.connect_ex((ip,port))
    if res == 0:
        return True
    else:
        return False

def check(i):
    parts = i.split(".")
    if len(parts) < 4 or len(parts) > 4:
        return False
    else:
        while len(parts) == 4:
            a = int(parts[0])
            b = int(parts[1])
            c = int(parts[2])
            d = int(parts[3])
            if a <= 0 or a == 127:
                return False
            elif d == 0:
                return False
            elif a >= 255:
                return False
            elif b >= 255 or b < 0:
                return False
            elif c >= 255 or c < 0:
                return False
            elif d >= 255 or c < 0:
                return False
            else:
                return True


@client.event
async def on_ready():
    print('Ready to H4CK')

@client.event
async def on_message(message):
    msg = message.content

    if message.author == client.user:
        return


    if message.content.startswith('$Hello'):
        await message.channel.send('The Fuck you want?')

    if msg.startswith('$Hack'):
        a = msg.split(" ")
        ip = a[1]
        port = a[2]
        protocol = a[3]


        if check(ip):
            await message.channel.send("Scanning " + ip + ":" + port)
            if port_scan(ip, int(port)):
                await message.channel.send("Port: {} open".format(port))
                await message.channel.send("Running: {}".format(GetServiceName(int(port),protocol)))
            else:
                await message.channel.send("Port is closed")
        else:
            await message.channel.send("Invalid ipv4 address")

    if msg.startswith('$Scan'):
        a = msg.split(" ")
        ip = a[1]


        if check(ip):
            await message.channel.send("Scanning " + ip)
            await message.channel.send(scanner(ip))
        else:
            await message.channel.send("Invalid ipv4 address")

    if msg.startswith('$Curl'):
        a = msg.split(" ")
        url = a[1]
        await message.channel.send(GetWebContent(url))

client.run('bot_token')
