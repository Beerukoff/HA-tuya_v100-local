"""V100 lock entity."""

from __future__ import annotations

from homeassistant.components.lock import LockEntity

from .device import V100Device


class V100Lock(LockEntity):
    """Tuya V100 smart lock."""

    def __init__(self, device: V100Device, name: str) -> None:
        self._device = device
        self._attr_name = name
        self._attr_unique_id = f"{name}_lock"

    @property
    def is_locked(self) -> bool | None:
        """Return lock state."""
        return not self._device.is_open()

    async def async_lock(self, **kwargs) -> None:
        """Lock."""
        await self.hass.async_add_executor_job(
            self._device.close
        )

    async def async_unlock(self, **kwargs) -> None:
        """Unlock."""
        await self.hass.async_add_executor_job(
            self._device.open_lock
        )

    async def async_update(self) -> None:
        """Update state."""
        await self.hass.async_add_executor_job(
            self._device.status
        )
