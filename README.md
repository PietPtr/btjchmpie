# btptr

An IRC bot written in python

# Commands

| Command    | Description                                               | Implemented |
|------------|-----------------------------------------------------------|-------------|
| !tell      | Sends a message to a user when they return                |N			   |
| !afk       | Marks a user Away From Keyboard                           |N			   |
| !back      | Marks a user back                                         |N		       |
| !where     | Checks where a user is (AFK or Back)                      |N			   |
| !choose    | Chooses one of the given options                          |Y			   |
| !answer    | (kindof)                                                  |N			   |
| !remind    | Reminds a user of something after a given amount of time  |N			   |
| !waitforit | stupid reference joke command                             |N			   |
| !whatsnew  | New functions in the bot                                  |N			   |
| !say       | Make the bot send a message                               |Y			   |
| !rejoin    | Rejoins the channel                                       |N			   |
| !ascii     | Turns a string into ASCII-art                             |Y*		   |
| !ok        | Prints "OK" in ASCII-art                                  |N			   |
| !pls       | Prints "PLS" in ASCII-art                                 |N			   |
| n1         | Prints "N1" in ASCII-art                                  |N			   |
| !lenny     | Prints a lenny face:  ( ͡° ͜ʖ ͡°)                            |N			   |
| !tableflip | Prints a table flip: (╯°□°）╯︵ ┻━┻                       |N			   |
| !quote     | Quote system                                              |N            |

Notes:
    !ascii:
        Due to a problem with the parser, special characters after or at the beginning
        of a word will fail to be parsed.
