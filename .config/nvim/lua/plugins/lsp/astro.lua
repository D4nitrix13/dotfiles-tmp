local astro_ls = vim.fn.exepath("astro-ls")

return {
  {
    "neovim/nvim-lspconfig",
    opts = {
      servers = {
        astro = {
          cmd = astro_ls ~= "" and { astro_ls, "--stdio" } or nil,
        },
      },
    },
  },
}
