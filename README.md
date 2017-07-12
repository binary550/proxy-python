![Python-Proxy](data/logo.jpg)

A frontend of proxychains-ng with python

## Documentation

### Manual

Pytho-Proxy allows you to set a random proxy or add your

Proxychains configuration is located in data/proxychains.template

All proxy are located in data/list


##### Example

You can use Python-Proxy to run a programm : 

> python-proxy -r firefox

Or just set a random proxy (when computer boot or with crontab) :

> python-proxy -r

If you want to set a specific proxy : 

> python-proxy -c socks5 127.0.0.1 1080

Or you can update proxy list :

> python-proxy -u

### To-Do

 + Proxy list update (from premproxy.net)
 + Same function for func_proxy.manual + .random

## License

This software is under the GNU GPL V3
