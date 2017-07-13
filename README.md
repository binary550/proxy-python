![Python-Proxy](logo.jpg)

A frontend of proxychains-ng writed with love with python3.6

## Documentation

### Manual

Python-Proxy allows you to set a random proxy or add your

Proxychains configuration is located in data/proxychains.template

All proxy are located in data/list, and html source are readable in data/index



##### Example

python-proxy has a built in update function (only socks4 support right now) :

----
python-proxy -u
----

You can list all your proxy list :

> python-proxy -l

Afterwards, you can run a program through a random proxy :

> python-proxy -r firefox

And check your ip :

> python-proxy -r curl -s checkip.amazonaws.com

Or if you want to connect with a custom proxy :

> python-proxy -c http 123.456.789.01 8080


### To-Do

 + ~~Proxy list update (from premproxy.net)~~
 + ~~Same function for func_proxy.manual + .random~~
 + ~~Program execution after python-proxy -r~~
 + Auto choose between HTTP, SOCKS4 and SOCKS5
 + ~~Display selected proxy~~

## License

This software is under the GNU GPL V3
