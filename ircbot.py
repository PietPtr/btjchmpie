#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    ircbot - irc bot class
    This file is part of btptr.

    Copyright (c) 2017 MrTijn

    Foobar is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Foobar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with btptr.  If not, see <http://www.gnu.org/licenses/>.
"""

import socket
import time
import random
import re

class ircbot:
    nickname = None
    channel = None
    owner = None
    irc_server_address = None
    irc_server_port = None

    # compiled regexes for optimisation
    command_regex = re.compile('PRIVMSG \#\S+ \:\!.*')
    quote_regex = re.compile('"')

    def __init__(self, nickname, channel, owner, irc_server_address, irc_server_port):
        self.nickname = nickname
        self.channel = channel
        self.owner = owner
        self.irc_server_address = irc_server_address
        self.irc_server_port = irc_server_port

    def connect(self, sock):
        sock.connect((self.irc_server_address, self.irc_server_port))
        sock.send("USER " + self.nickname + " 0 * :" + self.owner + "\r\n")
        sock.send("NICK " + self.nickname + "\r\n")

    def send_msg(self, msg, sock):
        """Send a string to the configured channel"""
        return sock.send("PRIVMSG " + self.channel + " :" + msg + "\r\n")

    def notice(self, msg, nick, sock):
        return sock.send("NOTICE " + nick + " :" + msg + "\r\n")

    def get_sender(self, msg):
        """Parse sender from given message"""
        # Maybe use a regex for this?
        return msg.split("!")[0].split(':')[1]

    def parse_arguments(self, data):
        """Parse all the arguments of an user-issued command

        Returns [command, [arguments]]
        data -- received raw data
        """

        # Example data:
        # :MrTijn!~MrTijn@unaffiliated/tijndagamer PRIVMSG #btjchmpy :!say this is a command

        # Retrieve the command and its arguments from the data
        command_and_args = command_regex.findall(data)[0].lstrip("PRIVMSG " + self.channel + ":!")
        command = command_and_args.split(' ')[0]

        # Second lstrip is to remove trailing whitespace
        arguments = command_and_args.lstrip(command).lstrip()
        if quote_regex.match(arguments) == None:
            # No arguments with quotes given, so this is easy
            arguments = arguments.split(' ')
        else:
            # todo
        return [command, arguments]

    def parse_recv_data(self, data, sock):
        if data[0:4] == "PING":
            sock.send(data.replace("PING", "PONG"))
        if data[0] != ':':
            continue
        if data.split(' ')[1] == "PRIVMSG":
            msg = data.split(' ')[3]
            if msg.startswith(":!"):
                arguments = self.parse_arguments(data)

                if command == ":!say":
                    self.command_say(arguments, sock)

    # Methods for user-commands

    def command_say(self, msg, sock):
        """Say what the user told us to say"""
        return self.send_msg(msg.split(':')[2], sock)

#    def command_choose(self, msg, sock):