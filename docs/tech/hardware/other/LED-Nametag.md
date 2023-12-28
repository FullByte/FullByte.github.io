# LED Name Tag

## Links

- <https://www.lednametags.de/>
- <https://lesun-led.en.alibaba.com/>
- <https://github.com/jnweiger/led-name-badge-ls32>

## Config

Add udev rule allowing anybody read/write access to the badge via USB:

``` sh
sudo cp 99-led-badge-44x11.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger
```

Install dependencies

``` sh
sudo apt install python3-usb python3-pil
sudo pip install pyhidapi
sudo pip install pillow
```

## Docs

usage: led-badge-11x44.py [-h] [-s SPEED] [-m MODE] [-b BLINK] [-a ANTS] [-p FILE] [-l] MESSAGE [MESSAGE ...]

- **MESSAGE** Up to 8 message texts with embedded builtin icons or loaded images within colons(:) -- See -l for a list of builtins
- **-s SPEED** Scroll speed (Range 1..8). Up to 8 comma-separated values
- **-m MODE** Up to 8 mode values: Scroll-left(0) -right(1) -up(2) -down(3); still-centered(4); animation(5); dropdown(6); curtain(7); laser(8); See '--mode-help' for  more details.
- **-b BLINK** 1: blinking, 0: normal. Up to 8 comma-separated values
- **-a ANTS** 1: animated border, 0: normal. Up to 8 comma-separated values
- **-l LIST** list named icons to be embedded in messages and exit

## Example

Hello World:

``` py
sudo python3 ./led-badge-11x44.py "Hello World!"
```

Beating Heart

``` py
sudo python3 ./led-badge-11-x44.py -b0,1 -s1 -m5 "  :heart2:    :HEART2:" "  :HEART2:"
```
