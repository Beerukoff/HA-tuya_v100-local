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

        try:
            self._device.set_version(float(version))
        except (TypeError, ValueError):
            self._device.set_version(3.4)

        self._device.set_socketPersistent(True)

    def status(self) -> dict:
        """Read DPS."""
        result = self._device.status()
        return result.get("dps", {})

    def is_open(self) -> bool:
        """Lock state."""
        return self.status().get("148", False)

    def open_lock(self):
        """Open lock."""
        return self._device.set_value(148, True)

    def disconnect(self):
        """Close connection."""
        self._device.close()
