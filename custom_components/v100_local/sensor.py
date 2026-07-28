"""Sensor platform for V100 Local."""

from homeassistant.components.sensor import SensorEntity

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up V100 sensors."""

    async_add_entities(
        [
            V100Sensor(entry.data["host"])
        ]
    )


class V100Sensor(SensorEntity):
    """Representation of a V100 sensor."""

    def __init__(self, host):
        self._host = host
        self._attr_name = f"V100 {host}"
        self._attr_native_value = "online"

    async def async_update(self):
        """Update sensor."""
        self._attr_native_value = "online"
