__version__ = '0.0.2'
__author__ = 'PyBots'
__email__ = 'support@pybots.ai'

from my_autopylot.CheckSystem import is_supported

compatible_system = is_supported()

if compatible_system:

    # # ---------  Message  Functions | Current Count : 4
    # from my_autopylot.Engine import message_pop_up
    # from my_autopylot.Engine import message_counter_down_timer
    # from my_autopylot.Engine import message_flash
    # from my_autopylot.Engine import message_toast

    # ---------  Mouse Functions | Current Count : 4
    from my_autopylot.Engine import mouse_click
    from my_autopylot.Engine import mouse_move
    from my_autopylot.Engine import mouse_drag_from_to
    from my_autopylot.Engine import mouse_search_snip_return_coordinates_x_y

    # ---------  Keyboard Functions | Current Count : 3
    from my_autopylot.Engine import key_press
    from my_autopylot.Engine import key_write_enter
    from my_autopylot.Engine import key_hit_enter

    # ---------  Browser Functions | Current Count : 1
    from my_autopylot.Engine import ChromeBrowser

    # ---------  Folder Functions | Current Count : 8
    from my_autopylot.Engine import folder_read_text_file
    from my_autopylot.Engine import folder_write_text_file
    from my_autopylot.Engine import folder_create
    from my_autopylot.Engine import folder_create_text_file
    from my_autopylot.Engine import folder_get_all_filenames_as_list
    from my_autopylot.Engine import folder_delete_all_files
    from my_autopylot.Engine import file_rename
    from my_autopylot.Engine import file_get_json_details

    # ---------  Window Operations Functions | Current Count : 8
    from my_autopylot.Engine import windows_show_desktop
    from my_autopylot.Engine import windows_launch_app
    from my_autopylot.Engine import window_get_active_window
    from my_autopylot.Engine import window_activate_window
    from my_autopylot.Engine import window_get_all_opened_titles_windows
    from my_autopylot.Engine import window_activate_and_maximize_windows
    from my_autopylot.Engine import window_minimize_windows
    from my_autopylot.Engine import window_close_windows

    # ---------  String Functions | Current Count : 3
    from my_autopylot.Engine import string_extract_only_alphabets
    from my_autopylot.Engine import string_extract_only_numbers
    from my_autopylot.Engine import string_remove_special_characters

    # --------- Screenscraping Functions | Current Count : 5
    from my_autopylot.Engine import scrape_save_contents_to_notepad
    from my_autopylot.Engine import screen_clear_search
    from my_autopylot.Engine import search_highlight_tab_enter_open
    from my_autopylot.Engine import find_text_on_screen

    # --------- Utility Functions | Current Count : 8
    from my_autopylot.Engine import find
    from my_autopylot.Engine import pause_program
    from my_autopylot.Engine import download_this_file
    from my_autopylot.Engine import clear_screen
    from my_autopylot.Engine import show_emoji
    from my_autopylot.Engine import print_with_magic_color
    from my_autopylot.Engine import install_module
    from my_autopylot.Engine import uninstall_module

    # --------- Voice Interface | Current Count : 2
    from my_autopylot.Engine import text_to_speech
    from my_autopylot.Engine import speech_to_text

# ---------  Excel Functions | Current Count : 18
    from my_autopylot.Engine import excel_get_row_column_count
    from my_autopylot.Engine import excel_copy_range_from_sheet
    from my_autopylot.Engine import excel_copy_paste_range_from_to_sheet
    from my_autopylot.Engine import excel_split_by_column
    from my_autopylot.Engine import excel_split_the_file_on_row_count
    from my_autopylot.Engine import excel_merge_all_files
    from my_autopylot.Engine import excel_drop_columns
    from my_autopylot.Engine import excel_clear_sheet
    from my_autopylot.Engine import excel_set_single_cell
    from my_autopylot.Engine import excel_get_single_cell
    from my_autopylot.Engine import excel_remove_duplicates
    from my_autopylot.Engine import excel_create_excel_file_in_given_folder
    from my_autopylot.Engine import excel_if_value_exists
    from my_autopylot.Engine import excel_to_colored_html
    from my_autopylot.Engine import excel_get_all_sheet_names
    from my_autopylot.Engine import excel_get_all_header_columns
    from my_autopylot.Engine import excel_describe_data
    from my_autopylot.Engine import isNaN
