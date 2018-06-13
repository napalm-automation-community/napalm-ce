[![PyPI](https://img.shields.io/pypi/v/napalm-ce.svg)](https://pypi.org/project/napalm-ce/)

# napalm-ce

This is a [NAPALM](https://github.com/napalm-automation/napalm) community driver for the Huawei CloudEngine Switch.


## Quick start

```shell
pip install napalm-ce
```

```python
from napalm import get_network_driver

driver = get_network_driver("ce")
device = driver(hostname='192.168.1.1', username='admin', password="Huawei123", optional_args = {'port': 22})
device.open()
facts = device.get_facts()
device.close()
```

Check the full [NAPALM Docs](https://napalm.readthedocs.io/en/latest/index.html) for more detailed instructions.

### Implemented API

* cli(commands)
* close()
* commit_config()
* compare_config()
* discard_config()
* get_arp_table()
* get_config(retrieve=u'all')
* get_environment()
* get_facts()
* get_interfaces()
* get_interfaces_counters()
* get_interfaces_ip()
* get_lldp_neighbors()
* get_mac_address_table()
* get_users()
* is_alive()
* load_merge_candidate(filename=None, config=None)
* load_replace_candidate(filename=None, config=None)
* open()
* ping(destination, source=u'', ttl=255, timeout=2, size=100, count=5, vrf=u'')
* rollback()


## Setting up a Lab Environment

You can download Huawei eNSP simulator for free from [Huawei website](http://support.huawei.com/enterprise/wn/network-management/ensp-pid-9017384/software) after make an account. You can learn how to install it by this [tutorial](https://www.youtube.com/watch?v=Yw8HPPwrzZU).


