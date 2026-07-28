"""V100 device."""

from __future__ import annotations

import tinytuya


class V100Device:
    """Local Tuya V100."""

    def __init__(
        self,
        ip: str,
        device_id: str,
        local_key: str,
        version: str = "3.4",
    ) -> None:

        self._device = tinytuya.Device(
            device_id,
            ip,
            local_key,
        )

        self._device.set_version(float(version))
        self._device.set_socketPersistent(True)

    def status(self):
        """Read DPS."""
        return self._device.status()

    def open_lock(self):
        """Open lock."""
        return self._device.set_value(148, True)

    def close(self):
        self._device.close()
