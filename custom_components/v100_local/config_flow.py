"""Config flow for V100 Local."""

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN, CONF_HOST, CONF_PORT, DEFAULT_PORT


class V100LocalConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for V100 Local."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""

        if user_input is not None:
            return self.async_create_entry(
                title=f"V100 {user_input[CONF_HOST]}",
                data=user_input,
            )

        schema = vol.Schema(
            {
                vol.Required(CONF_HOST): str,
                vol.Optional(
                    CONF_PORT,
                    default=DEFAULT_PORT,
                ): int,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )
