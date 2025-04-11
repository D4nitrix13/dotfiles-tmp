return {
  -- "conform.nvim",
  "stevearc/conform.nvim",
  opts = {
    formatters_by_ft = {
      python = { "ruff_format" },
      rust = { "rustfmt" },
      php = { "php_cs_fixer" },
    },

    formatters = {
      -- Configuration for the ruff_format
      ruff_format = {
        append_args = {
          "--config",
          "format.quote-style = 'single'",
        },
      },

      -- Configuration for the rustfmt
      rustfmt = {
        command = "rustfmt",
      },
    },
  },
}
