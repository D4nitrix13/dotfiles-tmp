return {
  {
    "neovim/nvim-lspconfig",
    opts = function(_, opts)
      opts.servers = opts.servers or {}

      opts.servers.ty = {
        mason = false,
        cmd = { "ty", "server" },
        filetypes = { "python" },
        root_markers = {
          "ty.toml",
          "pyproject.toml",
          "setup.py",
          "setup.cfg",
          "requirements.txt",
          ".git",
        },
      }
    end,
  },
}
