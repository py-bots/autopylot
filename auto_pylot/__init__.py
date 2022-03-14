__version__ = '0.0.1'
__author__ = 'PyBots'
__email__ = 'support@pybots.ai'

from auto_pylot.CheckSystem import is_supported

compatible_system = is_supported()

if compatible_system:

    # # ---------  Message  Functions | Current Count : 4
    # from auto_pylot.Engine import message_pop_up
    # from auto_pylot.Engine import message_counter_down_timer
    # from auto_pylot.Engine import message_flash
    # from auto_pylot.Engine import message_toast

    # ---------  Mouse Functions | Current Count : 4
    from auto_pylot.Engine import mouse_click
    from auto_pylot.Engine import mouse_move
    from auto_pylot.Engine import mouse_drag_from_to
    from auto_pylot.Engine import mouse_search_snip_return_coordinates_x_y

    # ---------  Keyboard Functions | Current Count : 3
    from auto_pylot.Engine import key_press
    from auto_pylot.Engine import key_write_enter
    from auto_pylot.Engine import key_hit_enter

    # ---------  Browser Functions | Current Count : 1
    from auto_pylot.Engine import ChromeBrowser

    # ---------  Folder Functions | Current Count : 8
    from auto_pylot.Engine import folder_read_text_file
    from auto_pylot.Engine import folder_write_text_file
    from auto_pylot.Engine import folder_create
    from auto_pylot.Engine import folder_create_text_file
    from auto_pylot.Engine import folder_get_all_filenames_as_list
    from auto_pylot.Engine import folder_delete_all_files
    from auto_pylot.Engine import file_rename
    from auto_pylot.Engine import file_get_json_details

    # ---------  Window Operations Functions | Current Count : 8
    from auto_pylot.Engine import windows_show_desktop
    from auto_pylot.Engine import windows_launch_app
    from auto_pylot.Engine import window_get_active_window
    from auto_pylot.Engine import window_activate_window
    from auto_pylot.Engine import window_get_all_opened_titles_windows
    from auto_pylot.Engine import window_activate_and_maximize_windows
    from auto_pylot.Engine import window_minimize_windows
    from auto_pylot.Engine import window_close_windows

    # ---------  String Functions | Current Count : 3
    from auto_pylot.Engine import string_extract_only_alphabets
    from auto_pylot.Engine import string_extract_only_numbers
    from auto_pylot.Engine import string_remove_special_characters

    # --------- Screenscraping Functions | Current Count : 5
    from auto_pylot.Engine import scrape_save_contents_to_notepad
    from auto_pylot.Engine import screen_clear_search
    from auto_pylot.Engine import search_highlight_tab_enter_open
    from auto_pylot.Engine import find_text_on_screen

    # --------- Utility Functions | Current Count : 8
    from auto_pylot.Engine import find
    from auto_pylot.Engine import pause_program
    from auto_pylot.Engine import download_this_file
    from auto_pylot.Engine import clear_screen
    from auto_pylot.Engine import show_emoji
    from auto_pylot.Engine import print_with_magic_color
    from auto_pylot.Engine import install_module
    from auto_pylot.Engine import uninstall_module

    # --------- Voice Interface | Current Count : 2
    from auto_pylot.Engine import text_to_speech
    from auto_pylot.Engine import speech_to_text

# ---------  Excel Functions | Current Count : 18
    from auto_pylot.Engine import excel_get_row_column_count
    from auto_pylot.Engine import excel_copy_range_from_sheet
    from auto_pylot.Engine import excel_copy_paste_range_from_to_sheet
    from auto_pylot.Engine import excel_split_by_column
    from auto_pylot.Engine import excel_split_the_file_on_row_count
    from auto_pylot.Engine import excel_merge_all_files
    from auto_pylot.Engine import excel_drop_columns
    from auto_pylot.Engine import excel_clear_sheet
    from auto_pylot.Engine import excel_set_single_cell
    from auto_pylot.Engine import excel_get_single_cell
    from auto_pylot.Engine import excel_remove_duplicates
    from auto_pylot.Engine import excel_create_excel_file_in_given_folder
    from auto_pylot.Engine import excel_if_value_exists
    from auto_pylot.Engine import excel_to_colored_html
    from auto_pylot.Engine import excel_get_all_sheet_names
    from auto_pylot.Engine import excel_get_all_header_columns
    from auto_pylot.Engine import excel_describe_data
    from auto_pylot.Engine import isNaN
