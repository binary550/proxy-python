![Py-Proxy](img/logo.jpg)

[![AUR](https://img.shields.io/aur/license/yaourt.svg?style=flat-square)]() [![Travis](https://img.shields.io/travis/rust-lang/rust.svg?style=flat-square)]()

A frontend of proxychains-ng writed with love with python3.6

## Documentation

### Introduction

Py-Proxy allows you to set a random proxy or add your.

Proxychains configuration is located in data/proxychains.template .

All proxy are located in data/list, and html source are readable in data/index .

For the time being, Py-Proxy only support socks4 connection with the random option (Http, socks4/5 are available with manually option, or you can edit proxy file).

### Example

py-proxy has a built in update function (only socks4 support right now) :

> py-proxy -u

You can list all your proxy list :

> py-proxy -l

Afterwards, you can run a program through a random proxy :

> py-proxy -r firefox

And check your ip :

> py-proxy -r curl -s checkip.amazonaws.com

Or if you want to connect with a custom proxy :

> py-proxy -c http 123.456.789.01 8080


### To-Do

 + ~~Proxy list update (from premproxy.com)~~
 + ~~Same function for func_proxy.manual + .random~~
 + ~~Program execution after py-proxy -r~~
 + ~~Display selected proxy~~
 + ~~Detect proxy online/offline~~
 + Auto choose between HTTP, SOCKS4 and SOCKS5

## License

This software is under the GNU GPL V3
