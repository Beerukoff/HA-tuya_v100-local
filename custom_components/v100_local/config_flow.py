"""Config flow for V100 Local."""

from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries

from .const import (
    DOMAIN,
    CONF_IP,
    CONF_DEVICE_ID,
    CONF_LOCAL_KEY,
    CONF_PROTOCOL_VERSION,
    DEFAULT_PROTOCOL_VERSION,
)


class V100LocalConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict | None = None,
    ):
        """Handle user setup."""

        if user_input is not None:
            return self.async_create_entry(
                title=f"V100 {user_input[CONF_IP]}",
                data=user_input,
            )

        schema = vol.Schema(
            {
                vol.Required(CONF_IP): str,
                vol.Required(CONF_DEVICE_ID): str,
                vol.Required(CONF_LOCAL_KEY): str,
                vol.Optional(
                    CONF_PROTOCOL_VERSION,
                    default=DEFAULT_PROTOCOL_VERSION,
                ): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )
