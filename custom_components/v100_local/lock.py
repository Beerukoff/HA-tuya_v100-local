"""V100 lock entity."""

from __future__ import annotations

from homeassistant.components.lock import LockEntity

from .device import V100Device
from . import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up lock."""

    data = hass.data[DOMAIN][entry.entry_id]

    device = V100Device(
        ip=data["ip"],
        device_id=data["device_id"],
        local_key=data["local_key"],
        version=data.get("version", "3.4"),
    )

    async_add_entities(
        [
            V100Lock(
                device,
                entry.title,
            )
        ]
    )


class V100Lock(LockEntity):
    """Tuya V100 lock."""

    def __init__(self, device, name):
        self._device = device
        self._attr_name = name
        self._attr_unique_id = f"{name}_lock"

    @property
    def is_locked(self):
        return not self._device.is_open()

    async def async_unlock(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._device.open_lock
        )

    async def async_lock(self, **kwargs):
        # Пока у V100 нет команды закрытия
        pass

    async def async_update(self):
        await self.hass.async_add_executor_job(
            self._device.status
        )
