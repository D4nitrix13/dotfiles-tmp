-- Pull in the wezterm API
local wezterm = require("wezterm")

local font_rules = {
    {
        intensity = 'Bold',
        italic = false,
        font = wezterm.font_with_fallback {
            family = 'Agave Nerd Font Mono',
            weight = 'Bold',
            italic = true,
        },
    },

    {
        intensity = 'Normal',
        italic = false,
        font = wezterm.font_with_fallback {
            family = 'JetBrainsMono Nerd Font Mono',
            weight = 'Bold',
            italic = true,
        },
    },
}

return font_rules