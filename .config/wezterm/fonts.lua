-- Pull in the wezterm API
local wezterm = require("wezterm")

local fonts = wezterm.font_with_fallback {
	-- Main fountain with ligatures
	'Agave Nerd Font Mono',
	'JetBrainsMono Nerd Font Mono',
	'Hack Nerd Font Mono',
	'Mononoki Nerd Font Mono',
}

return fonts