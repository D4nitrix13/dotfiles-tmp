local intelephense = vim.fn.exepath("intelephense")

if intelephense == "" then
  intelephense = vim.fn.expand("~/.local/bin/intelephense")
end

return {
  {
    "neovim/nvim-lspconfig",
    opts = {
      servers = {
        intelephense = {
          -- Importante: no dejar que Mason instale este servidor.
          mason = false,

          -- Usar el Intelephense instalado con npm.
          cmd = { intelephense, "--stdio" },

          settings = {
            intelephense = {
              files = {
                maxSize = 5000000,
              },
            },
          },
        },
      },
    },
  },
}
