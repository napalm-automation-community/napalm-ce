"""Test fixtures."""
from builtins import super

import pytest
from napalm.base.test import conftest as parent_conftest
from napalm.base.test.double import BaseTestDouble
from napalm.base.utils import py23_compat
from napalm_ce import ce


@pytest.fixture(scope='class')
def set_device_parameters(request):
    """Set up the class."""
    def fin():
        request.cls.device.close()
    request.addfinalizer(fin)

    request.cls.driver = ce.CEDriver
    request.cls.patched_driver = PatchedCEDriver
    request.cls.vendor = 'ce'
    parent_conftest.set_device_parameters(request)


def pytest_generate_tests(metafunc):
    """Generate test cases dynamically."""
    parent_conftest.pytest_generate_tests(metafunc, __file__)


class PatchedCEDriver(ce.CEDriver):
    """Patched CE Driver."""

    def __init__(self, hostname, username, password, timeout=60, optional_args=None):
        """Patched CE Driver constructor."""
        super().__init__(hostname, username, password, timeout, optional_args)

        self.patched_attrs = ['device']
        self.device = FakeCEDevice()

    def disconnect(self):
        """Disconnect device."""
        pass

    def is_alive(self):
        """Return a flag with the state of the SSH connection."""
        return {
            'is_alive': True  # In testing everything works..
        }

    def open(self):
        """Connect device."""
        pass


class FakeCEDevice(BaseTestDouble):
    """HUAWEI CloudEngine device test double."""

    def send_command(self, command, **kwargs):
        """Send command to device."""
        filename = '{}.txt'.format(self.sanitize_text(command))
        full_path = self.find_file(filename)
        result = self.read_txt_file(full_path)
        return py23_compat.text_type(result)

    def disconnect(self):
        """Disconnect from the device."""
        pass
