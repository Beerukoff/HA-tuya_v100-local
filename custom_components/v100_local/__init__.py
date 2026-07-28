"""V100 Local integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .device import V100Device
from .lock import V100Lock

DOMAIN = "v100_local"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> bool:
    """Set up V100."""

    device = V100Device(
        ip=entry.data["ip"],
        device_id=entry.data["device_id"],
        local_key=entry.data["local_key"],
        version=entry.data.get("version", "3.4"),
    )

    lock = V100Lock(
        device,
        entry.title,
    )

    await hass.config_entries.async_forward_entry_setups(
        entry,
        ["lock"],
    )

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = lock

    return True
