return {
  {
    "neovim/nvim-lspconfig",
    opts = {
      servers = {
        vtsls = {
          settings = {
            typescript = {
              preferences = {
                includePackageJsonAutoImports = "auto",
              },
            },
            javascript = {
              preferences = {
                includePackageJsonAutoImports = "auto",
              },
            },
          },
        },
      },
    },
  },
}
