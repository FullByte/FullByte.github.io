# IRC

## IRC clients

- mIRC (GUI) <https://www.mirc.com/>
- weechat (CLI): sudo apt-get install weechat

## Server/Channel

- [freenode#crypto](irc://irc.freenode.net:+7000/#crypto "irc://irc.freenode.net:+7000/##crypto")
- [darkscience-us2](irc://irc-eu-2.darkscience.net/#darkscience "irc://irc-eu-2.darkscience.net/darkscience")
- [darkscience-eu](irc://irc-us-east-2.darkscience.net/#darkscience "irc://irc-us-east-2.darkscience.net/darkscience")
- [freenode](ircs://chat.freenode.net:6697/#infra-talk "ircs://chat.freenode.net:6697/#infra-talk")
- [cyberia](ircs://irc.cyberia.is:6697/#cyberia "ircs://irc.cyberia.is:6697/#cyberia")
- [geekshed](irc://eu.geekshed.net:+6697 "irc://eu.geekshed.net:+6697")
- [dal](irc://irc.dal.net:+6697 "irc://irc.dal.net:+6697")
- [distributed](irc://irc.distributed.net:+994 "irc://irc.distributed.net:+994")
- [indymedia](irc://irc.indymedia.org:+6697 "irc://irc.indymedia.org:+6697")
- [link-net](irc://irc.link-net.org:+7000 "irc://irc.link-net.org:+7000")
- [oftc](irc://irc.oftc.net:+6697 "irc://irc.oftc.net:+6697")
- [rizon](irc://irc.rizon.net:+6697 "irc://irc.rizon.net:+6697")
- [theonering](irc://irc.theonering.net:+6697 "irc://irc.theonering.net:+6697")
- [efnet](irc://ssl.efnet.org:+9999 "irc://ssl.efnet.org:+9999")

## Register a Channel

In this example we use weechat to register a channel on server libra.chat

Configure weechat

```irc
/server add libera irc.libera.chat/6697 -ssl
/set irc.server.libera.autoconnect on
/set irc.server.libera.sasl_username "fab1"
/set irc.server.libera.sasl_password "password"
/set irc.server.libera.username "fab1"
/set irc.server.libera.realname "fab1"
/secure passphrase my-secret-passphrase
/set irc.server.libera.sasl_password "${sec.data.libera_password}"
/set irc.server.libera.autojoin "#my-new-channel"
```

Connect to libra chat, make sure your username is correct and register your user:

```irc
/connect libera
/nick fab1
/msg NickServ REGISTER password email@address.net
/msg NickServ VERIFY REGISTER fab11 your-code-by-mail
```

Join a channel and make yourself operator, then register the channel

```irc
/JOIN #my-new-channel
/op fab1
/msg ChanServ REGISTER #my-new-channel password
```

You can now make the channel private, secret and add a password:

```irc
/mode #my-new-channel +s
/mode #my-new-channel +p
/MODE #my-new-channel +k channel-password
```

To join the channel, now run this command:

```irc
/JOIN #my-new-channel channel-password
```
