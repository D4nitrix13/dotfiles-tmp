-- bootstrap lazy.nvim, LazyVim and your plugins
require("config.lazy")
vim.opt.timeoutlen = 1000
vim.opt.ttimeoutlen = 0

vim.opt.termguicolors = true

-- Ayu Theme
vim.g.ayucolor = "dark" -- Other: mirage | light

-- Material Theme
vim.g.material_theme_style = "darker"
-- Option: 'default', 'palenight', 'ocean', 'lighter', 'darker',
-- 'default-community', 'palenight-community', 'ocean-community',
-- 'lighter-community', 'darker-community'

vim.g.material_terminal_italics = 1

-- vim.lsp.set_log_level("debug")
-- require("lspconfig").intelephense.setup({})
