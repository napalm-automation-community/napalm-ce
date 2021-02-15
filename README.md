# napalm-ce

This is a [NAPALM](https://github.com/napalm-automation/napalm) community driver for the Huawei CloudEngine Switch.

## Requirements

Python 3.6+, napalm 3+

## Quick start

```shell
pip install -i https://test.pypi.org/simple/ napalm-ce
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
* get_arp_table(vrf='')
* get_config(retrieve='all', full=False, sanitized=False)
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

