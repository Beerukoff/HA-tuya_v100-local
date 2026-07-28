"""Config flow for V100 Local."""

from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS

from .const import DOMAIN


class V100LocalConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""

        if user_input is not None:
            return self.async_create_entry(
                title="V100 Lock",
                data=user_input,
            )

        schema = vol.Schema(
            {
                vol.Required(CONF_IP_ADDRESS): str,
                vol.Required("device_id"): str,
                vol.Required("local_key"): str,
                vol.Optional("version", default="3.4"): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )
