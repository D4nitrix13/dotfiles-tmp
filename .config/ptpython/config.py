from prompt_toolkit.filters import ViInsertMode
from prompt_toolkit.key_binding.key_processor import KeyPress
from prompt_toolkit.keys import Keys
from prompt_toolkit.styles import Style
from ptpython.layout import CompletionVisualisation

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# Historial De Comandos
# Warning:
#    ~/.ptpython/history is deprecated, move your history to /home/d4nitrix13/.local/share/ptpython/history

# Directory
# 
# Command
# ptpython3 --interactive --asyncio --vi --history-file $HOME/.local/share/ptpython/history; resetcursor

# https://stackoverflow.com/questions/59936089/how-to-read-history-in-ptpython-console#59937002

__all__ = ["configure"]

def configure(repl):
    """
    Configuration method. This is called during the start-up of ptpython.

    :param repl: `PythonRepl` instance.
    """
    # Show function signature (bool).
    repl.show_signature = True

    # Show docstring (bool).
    repl.show_docstring = True

    # Show the "[Meta+Enter] Execute" message when pressing [Enter] only
    # inserts a newline instead of executing the code.
    repl.show_meta_enter_message = True

    # Show completions. (NONE, POP_UP, MULTI_COLUMN or TOOLBAR)
    repl.completion_visualisation = CompletionVisualisation.POP_UP

    # Completion menu scroll offset.
    repl.completion_menu_scroll_offset = 0

    # Show line numbers.
    repl.show_line_numbers = True

    # Show status bar.
    repl.show_status_bar = True

    # Show the sidebar help.
    repl.show_sidebar_help = True

    # Swap light/dark colors on or off
    repl.swap_light_and_dark = False

    # Highlight matching parentheses.
    repl.highlight_matching_parenthesis = True

    # Line wrapping.
    repl.wrap_lines = True

    # Mouse support.
    repl.enable_mouse_support = True

    # Complete while typing.
    repl.complete_while_typing = True

    # Fuzzy and dictionary completion.
    repl.enable_fuzzy_completion = True
    repl.enable_dictionary_completion = True

    # Vi mode.
    repl.vi_mode = True

    # Enable modal cursor in Vi mode.
    repl.cursor_shape_config = "Beam"  # Usamos el cursor delgado como prefieres.

    # Paste mode (disable auto-whitespace after newlines).
    repl.paste_mode = False

    # Use the classic prompt.
    repl.prompt_style = "classic"  # 'classic' or 'ipython'

    # Don't insert a blank line after output.
    repl.insert_blank_line_after_output = True

    # History search enabled.
    repl.enable_history_search = True

    # Enable auto suggestions.
    repl.enable_auto_suggest = True

    # Enable open-in-editor.
    repl.enable_open_in_editor = True

    # System prompt.
    repl.enable_system_bindings = True

    # Confirm exit prompt.
    repl.confirm_exit = True

    # Input validation enabled.
    repl.enable_input_validation = True

    # Set color depth for true color.
    repl.color_depth = "DEPTH_24_BIT"  # True color.

    # Syntax highlighting enabled.
    repl.enable_syntax_highlighting = True

    # Vi navigation mode on start.
    repl.vi_start_in_navigation_mode = True

    # Custom UI color scheme.
    _custom_ui_colorscheme = {
        "completion-menu.completion": "bg:#282c34 #abb2bf",
        "completion-menu.completion.current": "bg:#61afef #000000",
        "completion-menu.meta.completion": "bg:#282c34 #56b6c2",
        "completion-menu.meta.completion.current": "bg:#61afef #ffffff",
        "docstring": "bg:#000000 #98c379",
    }


    repl.install_ui_colorscheme("my-colorscheme", Style.from_dict(_custom_ui_colorscheme))
    repl.use_ui_colorscheme("my-colorscheme")

    # Define custom syntax highlighting with custom colors
    _custom_style = Style.from_dict({
        # Strings
        'string': 'bg:#282c34 #98c379 italic bold',
        'string.escape': 'bg:#282c34 #98c379 italic bold',
        'string.special': 'bg:#282c34 #98c379 italic bold',

        # Variables y tipos
        'variable': 'bg:#282c34 #61afef italic bold',
        'type': 'bg:#282c34 #d19a66 italic bold',
        'operator': 'bg:#282c34 #e06c75 italic bold',

        # Funciones y clases
        'name.function': 'bg:#282c34 #61afef italic bold',
        'name.class': 'bg:#282c34 #c678dd italic bold',
        'name.namespace': 'bg:#282c34 #56b6c2 italic bold',

        # Resaltado de variables y operadores específicos
        'keyword.operator': 'bg:#282c34 #e06c75 italic bold',
        'keyword': 'bg:#282c34 #c678dd italic bold',

        # Apply italic and bold to specific scopes like comments, keywords, etc.
        'comment': 'bg:#282c34 #7f8c8d italic bold',
        'keyword': 'bg:#282c34 #c678dd italic bold',

        # Syntax error (highlighted in red)
        'error': 'bg:#282c34 #e06c75 italic bold',
    })

    repl.style = _custom_style

    # Highlight type annotations with colors
    repl.highlight_type_annotations = True

    # Auto-completion with detailed info and highlighted items
    repl.complete_while_typing = True
    repl.completion_visualisation = CompletionVisualisation.POP_UP

    # Highlight the cursor when moving.
    repl.cursor_shape_config = "Beam"  # Use a thin beam cursor as per your preference.

    # Custom color scheme for function arguments and docstring details
    repl.use_code_colorscheme("native")  # A good dark theme

    # Reset cursor style after typing
    repl.cursor_shape = 'beam'
