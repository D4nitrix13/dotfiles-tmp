return {
  {
    "adalessa/laravel.nvim",
    dependencies = {
      "MunifTanjim/nui.nvim",
      "nvim-lua/plenary.nvim",
      "nvim-neotest/nvim-nio",
    },
    ft = { "php", "blade" },
    event = { "BufReadPre artisan", "BufReadPre composer.json" },
    keys = {
      { "<leader>ll", function() Laravel.pickers.laravel() end, desc = "Laravel" },
      { "<leader>la", function() Laravel.pickers.artisan() end, desc = "Laravel Artisan" },
      { "<leader>lr", function() Laravel.pickers.routes() end, desc = "Laravel Routes" },
      { "<leader>lm", function() Laravel.pickers.make() end, desc = "Laravel Make" },
    },
    opts = {
      features = {
        pickers = {
          provider = "fzf_lua",
        },
      },
    },
  },
}
