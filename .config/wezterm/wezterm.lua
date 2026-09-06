-- Autor: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Gitlab: https://gitlab.com/D4nitrix13
-- Correo electrónico: danielperezdev@proton.me

-- Pull in the wezterm API
local wezterm = require("wezterm")

-- This table will hold the configuration.
local config = {}

-- In newer versions of wezterm, use the config_builder which will
-- help provide clearer error messages
if wezterm.config_builder then
	config = wezterm.config_builder()
end

local mux = wezterm.mux

config.native_macos_fullscreen_mode = true

-- This is where you actually apply your config choices
config.window_padding = {
	top = 10,
	right = 10,
	left = 10,
	bottom = 10
}

config.force_reverse_video_cursor = true

config.colors = require("colorscheme")
config.font = require("fonts")
config.font_rules = require("font_rules")

-- https://wezfurlong.org/wezterm/config/fonts.html
config.window_background_opacity = 0.85

-- https://wezfurlong.org/wezterm/config/lua/config/font_size.html
config.font_size = 20.0

-- config.font = wezterm.font("IosevkaTerm NFM")
config.hide_tab_bar_if_only_one_tab = true

-- https://wezfurlong.org/wezterm/config/lua/config/default_cursor_style.html
-- Acceptable values are SteadyBlock, BlinkingBlock, SteadyUnderline, BlinkingUnderline, SteadyBar, and BlinkingBar.
config.default_cursor_style = 'BlinkingBar'

-- https://wezfurlong.org/wezterm/config/lua/config/cursor_thickness.html
config.cursor_thickness = "0.1cell"

-- https://wezfurlong.org/wezterm/config/lua/config/underline_thickness.html
config.underline_thickness = "0.1cell"

-- https://wezfurlong.org/wezterm/config/lua/config/animation_fps.html
config.animation_fps = 60
config.cursor_blink_rate = 100
config.cursor_blink_ease_in = 'Constant'
config.cursor_blink_ease_out = 'Constant'

-- wezterm.on('gui-startup', function(cmd)
-- 	local tab, pane, window = mux.spawn_window(cmd or {})
-- 	local gui_window = window:gui_window()
-- 	gui_window:perform_action(wezterm.action.ToggleFullScreen, pane)
-- end
-- )

-- activate ONLY if windows --

-- config.default_domain = 'WSL:Ubuntu'
-- config.front_end = "OpenGL"

-- and finally, return the configuration to wezterm
return config
