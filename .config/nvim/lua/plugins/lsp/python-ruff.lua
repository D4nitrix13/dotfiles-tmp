return {
  {
    "neovim/nvim-lspconfig",
    opts = function(_, opts)
      opts.servers = opts.servers or {}

      opts.servers.ruff = {
        mason = false,
        cmd = { "ruff", "server" },
        filetypes = { "python" },
        root_markers = {
          "pyproject.toml",
          "ruff.toml",
          ".ruff.toml",
          "setup.py",
          "setup.cfg",
          "requirements.txt",
          ".git",
        },
      }
    end,
  },
}
