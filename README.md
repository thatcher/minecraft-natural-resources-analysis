# Distribution of Natural Resources in Minecraft Pi

This is a science fair project for my son Weilun to focus on the subject of
Computer Science -- Statistics.  I'll be doing the heavy lifting but the focus
is to introduce concepts of counting, averaging, and graphs leveraging his
passion for Minecraft.

Thanks for any feedback from Minecraft fans and programmers, and for any other
science fair moms and dads, please feel free to use this.  We are using the
simple [MIT License] so have at.

Thanks again,
[Thatcher]

[MIT License]: http://opensource.org/licenses/MIT
[Thatcher]: http://github.com/thatcher/

## Connecting to your Raspberry Pi

Once you have your Pi on your local network, and you've started the Minecraft Pi
game, you can actually do the rest of the work on another computer, talking to
the Mincraft server over the network.

All you need to know to connect is the Pi's network address.  The simplest way
is to run **ifconfig** from your Pi's Terminal.

```

$ ifconfig
...
en1: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
  ether 20:c9:d0:e5:7e:85
  inet6 fe80::22c9:d0ff:fee5:7e85%en1 prefixlen 64 scopeid 0x6
  inet 192.168.1.12 netmask 0xffffff00 broadcast 192.168.1.255
  nd6 options=1<PERFORMNUD>
  media: autoselect
  status: active
...

```

You get a lot of output, but the relevant section is above.  Most home networks
will assign your Pi an address like 192.168.1.12 (not 192.168.1.255, thats the
router itself.)

Now you can change your settings.py file:

```{python}
SERVER_ADDRESS = "192.168.1.12"
```

### SSH
SSH is probably the most effective way to log on to your Pi to check CPU load,
make sure processes arent stuck, etc.

### Remote Desktop
We have a keyboard setup on our Pi and its connected to our TV, but everyone
competes for the TV so we wanted to be able to check on the Pi via a Remote
Descktop.  This link helped us set up a vnc server:

http://computers.tutsplus.com/tutorials/take-control-of-your-raspberry-pi-using-your-mac-pc-ipad-or-phone--mac-54603

You can then connect to your Pi with Safari which has a built-in vnc client:

http://www.davidtheexpert.com/post.php?id=5
