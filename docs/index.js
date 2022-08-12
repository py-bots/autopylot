URLS=[
"my_autopylot/index.html",
"my_autopylot/chrome39.html",
"my_autopylot/citrix39.html",
"my_autopylot/clipboard39.html",
"my_autopylot/converters39.html",
"my_autopylot/excel39.html",
"my_autopylot/folder39.html",
"my_autopylot/keyboard39.html",
"my_autopylot/mail39.html",
"my_autopylot/message39.html",
"my_autopylot/mouse39.html",
"my_autopylot/pdf39.html",
"my_autopylot/screen_scraping39.html",
"my_autopylot/string39.html",
"my_autopylot/utility39.html",
"my_autopylot/voice39.html",
"my_autopylot/windows39.html"
];
INDEX=[
{
"ref":"my_autopylot",
"url":0,
"doc":""
},
{
"ref":"my_autopylot.chrome39",
"url":1,
"doc":""
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser",
"url":1,
"doc":""
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.open_browser",
"url":1,
"doc":"Description: This function opens a browser. Args: dummy_browser (bool, optional): True to open dummy browser. Defaults: True. profile (str, optional): Profile name to open. Defaults: \"Default\". incognito (bool, optional): True to open incognito browser. Defaults: False. Returns: [status, browser_driver] status (bool): Whether the function is successful or failed. browser_driver (object): The browser driver object.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.navigate",
"url":1,
"doc":"Description: Navigate through the url after the session is started. Args: url (str, optional): Url which you want to visit. Defaults:  . Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.write",
"url":1,
"doc":"Description: Write a string in browser, if user_visible_text_element is given it writes on the given element. Args: text (str, optional): String which has be written. Defaults:  . user_visible_text_element (str, optional): The element which is visible(Like : Sign in). Defaults:  . Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.set_download_path",
"url":1,
"doc":"Set the download path for the browser. Args: path (str, optional): The path to set. Defaults:  . Returns: bool: Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.mouse",
"url":1,
"doc":"Description: Performs a Mouse Click on the given value. Args: value (str, optional): The value which has to be clicked. Defaults:  . action_type (str, optional): The type of click. Defaults: \"single\". value_type (str, optional): The type of value. Defaults: \"text\". Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.mouse_v2",
"url":1,
"doc":"Description: Performs a Mouse Click on the given value. Args: value (str, optional): The value which has to be clicked. Defaults:  . action_type (str, optional): The type of click. Defaults: \"single\". value_type (str, optional): The type of value. Defaults: \"text\". Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.scroll",
"url":1,
"doc":"Description: Scrolls the browser window. Args: direction (str, optional): The direction to scroll. Defaults: \"down\".u,d,l,r weight : The weight of the scroll. Defaults: 3. 3 corresponds to 300 pixs Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.key_press",
"url":1,
"doc":"Description: Type text using Browser Helium Functions and press hot keys. Args: key_1 (str): Keys you want to simulate or string you want to press Eg: \"tab\" or \"Murali\". Defaults:  key_2 (str, optional): Key you want to simulate with combination to key_1. Eg: \"shift\" or \"escape\". Defaults:  Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.hit_enter",
"url":1,
"doc":"Description: Hits enter KEY in Browser Args: None Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.wait_until",
"url":1,
"doc":"Description: Wait until a specific element is found. Args: text (str, optional): To wait until the string appears on the screen. Eg: Export Successful Completed. Defaults:  element (str, optional): Type of Element Whether its a Text(t) or Button(b). Defaults: \"t - Text\". Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.check_if",
"url":1,
"doc":"Description: Check if a specific element is found. Args: text (str, optional): To wait until the string appears on the screen. Eg: Export Successful Completed. Defaults:  element (str, optional): Type of Element Whether its a Text(t) or Button(b). Defaults: \"t - Text\". Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.refresh_page",
"url":1,
"doc":"Description: Refresh the current active browser page. Args: None Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.set_waiting_time",
"url":1,
"doc":"Description: Set the waiting time for the self.browser_driver. If element is not found in the given time, it will raise an exception. Args: time ([int]): The time in seconds to wait for the element to be found. Defaults: 10 Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.get_text",
"url":1,
"doc":"Description: Get the text of the element. Args: element_xpath (str, optional): The xpath of the element. Defaults:  Returns: [status, data] status (bool): Whether the function is successful or failed. data (str): The text of the element.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.get_element_image",
"url":1,
"doc":"Get the image of the element. Args: element_xpath (str, optional): The xpath of the element. Defaults:  Returns: bool: Whether the function is successful or failed. str: The image of the element.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.close",
"url":1,
"doc":"Description: Close the current active browser. Args: None Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.chrome39.ChromeBrowser.get_value_relatively",
"url":1,
"doc":"Description: Text Element : Get the value of the element Link Element : Get the text of the element Button Element : Performs single left click on the element Args: element_type (str, optional): The type of the element. Defaults: \"Text\". above (str, optional): The xpath of the element above. Defaults:  . below (str, optional): The xpath of the element below. Defaults:  . to_left_of (str, optional): The xpath of the element to the left of. Defaults:  . to_right_of (str, optional): The xpath of the element to the right of. Defaults:  . Returns: [status, data] status (bool): Whether the function is successful or failed. data (str): The value of the element.",
"func":1
},
{
"ref":"my_autopylot.citrix39",
"url":2,
"doc":""
},
{
"ref":"my_autopylot.citrix39.clipboard_set_data",
"url":2,
"doc":"Description: Set data to clipboard Args: data: data to be set to clipboard format_id: format of data Returns: [status] status (bool) - True if successful, False if not",
"func":1
},
{
"ref":"my_autopylot.citrix39.clipboard_get_data",
"url":2,
"doc":"Description: Get data from clipboard Args: format_id: format of data Returns: [status, data] status (bool) - True if successful, False if not data (str) - data from clipboard",
"func":1
},
{
"ref":"my_autopylot.citrix39.citrix_scrape_contents_by_search_copy_paste",
"url":2,
"doc":"Description: Gets the focus on the Citrix screen/window by searching desired text using crtl+f and performs copy/paste of all data. Useful in Citrix applications This is useful in Citrix systems Args: highlight_text: text to be searched and highlighted Returns: [status, data] status (bool) - True if successful, False if not data (str) - Scraped data",
"func":1
},
{
"ref":"my_autopylot.citrix39.citrix_window_clear_search",
"url":2,
"doc":"Description: Clears previously found text (crtl+f highlight) Args: None Returns: [status] status (bool) - True if successful, False if not",
"func":1
},
{
"ref":"my_autopylot.clipboard39",
"url":3,
"doc":""
},
{
"ref":"my_autopylot.clipboard39.clipboard_set_data",
"url":3,
"doc":"Description: Set data to clipboard Args: data: data to be set to clipboard format_id: format of data Returns: [status] status (bool) - True if successful, False if not",
"func":1
},
{
"ref":"my_autopylot.clipboard39.clipboard_get_data",
"url":3,
"doc":"Description: Get data from clipboard Returns: [status, data] status (bool) - True if successful, False if not data (str) - data from clipboard",
"func":1
},
{
"ref":"my_autopylot.converters39",
"url":4,
"doc":""
},
{
"ref":"my_autopylot.converters39.convert_csv_to_excel",
"url":4,
"doc":"Args: input_file (str): [description]. Defaults to  . sep (str): [description]. Defaults to  . output_folder (str, optional): [description]. Defaults to  . output_filename (str, optional): [description]. Defaults to  . contains_header (bool,optional):[description]. Defaults to True Returns: [bool]: [status]",
"func":1
},
{
"ref":"my_autopylot.converters39.get_image_from_base64",
"url":4,
"doc":"Description: Convert base64 string to image. Args: imgFileName (str, optional): [description]. Defaults to  . input_file (str, optional): [description]. Defaults to  . output_folder (str, optional): [description]. Defaults to  . Returns: [bool]: [status]",
"func":1
},
{
"ref":"my_autopylot.converters39.convert_image_to_base64",
"url":4,
"doc":"Description: Convert image to base64 string. Args: input_file (str, optional): [description]. Defaults to  . Returns: [bool]: [status]",
"func":1
},
{
"ref":"my_autopylot.converters39.excel_change_corrupt_xls_to_xlsx",
"url":4,
"doc":"Repair corrupt file to regular file and then convert it to xlsx. status : Done.",
"func":1
},
{
"ref":"my_autopylot.converters39.excel_convert_xls_to_xlsx",
"url":4,
"doc":"Converts given XLS file to XLSX",
"func":1
},
{
"ref":"my_autopylot.converters39.convert_image_jpg_to_png",
"url":4,
"doc":"Convert the image from jpg to png Args: input_image_path (str): The path of the input image output_folder_path (str): The path of the output folder Returns: [bool]: Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.converters39.convert__image_png_to_jpg",
"url":4,
"doc":"Convert the image from png to jpg Args: input_image_path (str): The path of the input image output_folder_path (str): The path of the output folder Returns: [bool]: Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.converters39.excel_to_colored_html",
"url":4,
"doc":"Converts given Excel to HTML preserving the Excel format and saves in same folder as .html",
"func":1
},
{
"ref":"my_autopylot.excel39",
"url":5,
"doc":""
},
{
"ref":"my_autopylot.excel39.authenticate_google_spreadsheet",
"url":5,
"doc":"Description: Authenticates Google Spreadsheet. Args: credential_file_path (str, optional): Path of credential file. Defaults to  . Returns: [status, data] status (bool): Whether the function is successful or failed. data (object): Google Spreadsheet Auth object.",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_get_dataframe_from_google_spreadsheet",
"url":5,
"doc":"Description: Get dataframe from google spreadsheet. Args: URL (str, optional): (Only in Windows)Name of Window you want to activate. Eg: Notepad. Defaults to  . Returns: [status, data] status (bool): Whether the function is successful or failed. data (object): Dataframe object.",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_tabular_data_from_website",
"url":5,
"doc":"Description: Gets Website Table Data Easily as an Excel using Pandas. Just pass the URL of Website having HTML Tables. Args: website_url (str, optional): URL of Website. Defaults to  . table_number (int, optional): Table Number. Defaults to all. Returns: [status, data] status (bool): Whether the function is successful or failed. data (object): Dataframe object.",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_upload_dataframe_to_google_spreadsheet",
"url":5,
"doc":"Description: Uploads dataframe to google spreadsheet. Args: URL (str, optional): (Only in Windows)Name of Window you want to activate. Eg: Notepad. Defaults to  . Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_create_file",
"url":5,
"doc":"Description: Creates an Excel file. Args: output_folder (str, optional): Folder where file will be created. Defaults to  . output_filename (str, optional): Name of file. Defaults to  . output_sheetname (str, optional): Name of sheet. Defaults to \"Sheet1\". Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_to_dataframe",
"url":5,
"doc":"Description: Converts excel to dataframe Args: input_filepath (str) : Complete path to the excel file. input_sheetname (str) : Sheet name of the excel file. header (int) : Row number of the header. Returns: [status, data] status (bool): Whether the function is successful or failed. data (pandas dataframe): Dataframe of the excel file.",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_get_row_column_count",
"url":5,
"doc":"Description: Returns the row and column count of the dataframe. Args: df (pandas dataframe): Dataframe of the excel file. Returns: [status, data] status (bool): Whether the function is successful or failed. data (list): [row_count, column_count]",
"func":1
},
{
"ref":"my_autopylot.excel39.dataframe_to_excel",
"url":5,
"doc":"Description: Converts dataframe to excel Args: df (pandas dataframe): Dataframe of the excel file. output_folder (str, optional): Folder path of the output file. Defaults to  . output_filename (str, optional): Filename of the output file. Defaults to  . output_sheetname (str, optional): Sheetname of the output file. Defaults to \"Sheet1\". mode (str, optional): Mode of the output file. Defaults to \"a\" or \"x\" Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_set_single_cell",
"url":5,
"doc":"Description: Writes the given text to the desired column/cell number for the given excel file Args: df (pandas dataframe): Dataframe of the excel file. column_name (str, optional): Column name of the excel file. Defaults to  . cell_number (int, optional): Cell number of the excel file. Defaults to 1. text (str, optional): Text to be written to the excel file. Defaults to  . Returns: [status, data] status (bool): Whether the function is successful or failed. data (df): Modified dataframe",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_get_single_cell",
"url":5,
"doc":"Description: Gets the text from the desired column/cell number of the given excel file Args: df (pandas dataframe): Dataframe of the excel file. header (int, optional): Header of the excel file. Defaults to 0. column_name (str, optional): Column name of the excel file. Defaults to  . cell_number (int, optional): Cell number of the excel file. Defaults to 0. Returns: [status, data] status (bool): Whether the function is successful or failed. data (str): Data from the desired column/cell number of the excel file.",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_get_all_header_columns",
"url":5,
"doc":"Description: Gives you all column header names of the given excel sheet. Args: df (pandas dataframe): Dataframe of the excel file. Returns: [status, data] status (bool): Whether the function is successful or failed. data (list): List of all column header names of the excel file.",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_get_all_sheet_names",
"url":5,
"doc":"Description: Gives you all names of the sheets in the given excel sheet. Parameters: input_filepath (str) : Path of the excel file. returns : [status, data] status (bool): Whether the function is successful or failed. data (list): List of all sheet names of the excel file.",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_copy_range_from_sheet",
"url":5,
"doc":"Description: Copies the specific range from the provided excel sheet and returns copied data as a list Args: input_filepath :\"Full path of the excel file with double slashes\" input_sheetname :\"Source sheet name from where contents are to be copied\" start_col :\"Starting column number (index starts from 1) from where copying starts\" start_row :\"Starting row number (index starts from 1) from where copying starts\" end_col :\"Ending column number ex:4 upto where cells to be copied\" end_row :\"Ending column number ex:5 upto where cells to be copied\" Returns: [status, data] status (bool): Whether the function is successful or failed. data (list): Range of cells as a list.",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_paste_range_to_sheet",
"url":5,
"doc":"Description: Pastes the copied data in specific range of the given excel sheet. Args: input_filepath :\"Full path of the excel file with double slashes\" input_sheetname :\"Source sheet name from where contents are to be copied\" start_col :\"Starting column number (index starts from 1) from where copying starts\" start_row :\"Starting row number (index starts from 1) from where copying starts\" copied_data :\"The copied data to be pasted\" Returns: [status, data] status (bool): Whether the function is successful or failed. data (list): Range of cells as a list.",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_group_by_column_values_n_split",
"url":5,
"doc":"Description: This function groups the dataframe by the given column and splits the dataframe into multiple dataframes. Parameters: df : dataframe column_name : column name to be grouped output_folder : folder path to save the split dataframes output_filename : filename to save the split dataframes Returns: [status] status : True if the function is successful, False otherwise",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_merge_all_files",
"url":5,
"doc":"Description: Merges all the excel files in the given folder Args: input_folder_path :\"Full path of the folder with double slashes\" output_folder :\"Full path of the folder with double slashes\" output_filename :\"Filename to save the merged excel file\" Returns: [status] status : True if the function is successful, False otherwise",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_drop_columns",
"url":5,
"doc":"Description: Drops the desired column from the given excel file Parameters: df : dataframe cols : column names to be dropped Returns: [status, data] status : True if the function is successful, False otherwise data : dataframe with the dropped columns",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_clear_sheet",
"url":5,
"doc":"Description: Clears the contents of given excel files keeping header row intact Args: df : dataframe Returns: [status, data] status : True if the function is successful, False otherwise data : dataframe with the cleared contents",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_remove_duplicates",
"url":5,
"doc":"Description: Drops the duplicates from the desired Column of the given excel file Args: df : dataframe column_name : column name from which duplicates are to be removed Returns: [status, data] status : True if the function is successful, False otherwise data : dataframe with the duplicates removed",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_if_value_exists",
"url":5,
"doc":"Description: Check if a given value exists in given excel. Returns True / False Args: df : dataframe cols : column name from which the value is to be checked value : value to be checked Returns: [status] status : True if the value exists, False otherwise",
"func":1
},
{
"ref":"my_autopylot.excel39.isNaN",
"url":5,
"doc":"Description: Returns TRUE if a given value is NaN False otherwise Parameters: value : value to be checked Returns: [status] status : True if the value is NaN, False otherwise",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_apply_format_as_table",
"url":5,
"doc":"Description: Applies table format to the used range of the given excel. Just it takes an path and converts it to table here you can change the table style below. if you want to change the table style just change the styles by refering excel Args: input_filepath : path of the excel file table_style : table style to be applied input_sheetname : sheet name of the excel file Returns: [status] status : True if the function is successful, False otherwise",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_apply_template_format",
"url":5,
"doc":"Description: Converts given excel to Template Excel This function uses pandas and just write the required columns to new excel. if you don't know columns, just pass the excel file which have the columns you want it automatically makes own list and remove other columns. Args: input_filepath : path of the excel file input_sheetname : sheet name of the excel file input_template_filepath : path of the template excel file input_template_sheetname : sheet name of the template excel file same_file : if True, then the output excel file will be same as the input excel file. output_folder : folder path where the output excel file will be saved. output_filename : name of the output excel file. Returns: [status] status : True if the function is successful, False otherwise",
"func":1
},
{
"ref":"my_autopylot.excel39.df_from_list",
"url":5,
"doc":"Description: Creates a dataframe from a list of lists Args: list_of_lists : list of lists column_names : list of column names Returns: [data] data : dataframe object",
"func":1
},
{
"ref":"my_autopylot.excel39.df_from_string",
"url":5,
"doc":"Description: Creates a dataframe from a string Args: df_string : string word_delimeter : word delimeter line_delimeter : line delimeter column_names : list of column names Returns: [data] data : dataframe object",
"func":1
},
{
"ref":"my_autopylot.excel39.df_extract_sub_df",
"url":5,
"doc":"Description: Extracts a sub dataframe from a dataframe Args: df : dataframe row_start : start row number row_end : end row number column_start : start column number column_end : end column number Returns: [data] data : dataframe object",
"func":1
},
{
"ref":"my_autopylot.excel39.set_value_in_df",
"url":5,
"doc":"Description: Sets a value in a dataframe Args: df : dataframe row_number : row number column_number : column number value : value to be set Returns: [data] data : dataframe object",
"func":1
},
{
"ref":"my_autopylot.excel39.get_value_in_df",
"url":5,
"doc":"Description: Gets a value from a dataframe Parameters: df : dataframe row_number : row number column_number : column number Returns: [data] data : value from dataframe",
"func":1
},
{
"ref":"my_autopylot.excel39.excel_concat_all_sheets_of_given_excel",
"url":5,
"doc":"Description: Concatenates all sheets of an excel file Args: excel_file_path : excel file path Returns: [data] data : dataframe object",
"func":1
},
{
"ref":"my_autopylot.excel39.df_drop_rows",
"url":5,
"doc":"Description: Drops a range of rows from a dataframe including the row_start and row_end rows. Args: df : dataframe row_start : start row number row_end : end row number Returns: [data] data : dataframe object",
"func":1
},
{
"ref":"my_autopylot.excel39.df_convert_column_to_type",
"url":5,
"doc":"Description: Converts a column type of a dataframe to a given type Column type doesn't persist after writing to excel Args: df : dataframe column_name : Single column name or list of column names column_type : column type to be converted to like string, int, float, date, boolean, complex, bytes, etc. Returns: [data] data : The modified dataframe object",
"func":1
},
{
"ref":"my_autopylot.excel39.df_vlookup",
"url":5,
"doc":"Description: Performs vlookup on 2 dataframes Args: df1 : dataframe df2 : dataframe column_name : column name to perform vlookup on how : how to perform vlookup like inner, left, right, outer Returns: [data] data : The modified dataframe object",
"func":1
},
{
"ref":"my_autopylot.folder39",
"url":6,
"doc":""
},
{
"ref":"my_autopylot.folder39.folder_read_text_file",
"url":6,
"doc":"Description: Reads from a given text file and returns entire contents as a single list Args: txt_file_path (str) : path to the text file. Returns: [status, data] status (bool) - True if the file is read successfully. data (List) - list of all the contents of the text file.",
"func":1
},
{
"ref":"my_autopylot.folder39.folder_write_text_file",
"url":6,
"doc":"Description: Writes to a given text file and returns entire contents as a single list Args: txt_file_path (str) : path to the text file. contents (str) : contents to be written to the text file. Returns: [status, data] status (bool) - True if the file is read successfully. data (List) - list of all the contents of the text file.",
"func":1
},
{
"ref":"my_autopylot.folder39.folder_create",
"url":6,
"doc":"Description: while making leaf directory if any intermediate-level directory is missing, folder_create() method will create them all. Args: folderPath (str) : path to the folder where the folder is to be created. Returns: [status] status (bool) - True if the folder is created successfully.",
"func":1
},
{
"ref":"my_autopylot.folder39.folder_create_text_file",
"url":6,
"doc":"Description: Creates Text file in the given path. Internally this uses folder_create() method to create folders if the folder/s does not exist. automatically adds txt extension if not given in textFilePath. Args: textFolderPath (str) : path to the folder where the text file is to be created. txtFileName (str) : name of the text file. custom (bool) : True if the text file name is to be customised. Returns: [status] status (bool) - True if the file is created successfully.",
"func":1
},
{
"ref":"my_autopylot.folder39.folder_get_all_filenames_as_list",
"url":6,
"doc":"Description: Get all the files of the given folder in a list. Args: strFolderPath (str) : Location of the folder. extension (str) : extention of the file. by default all the files will be listed regarless of the extension. Returns: [status, data] status (bool) - True if the file is read successfully. data (List) - list of all the files in the folder.",
"func":1
},
{
"ref":"my_autopylot.folder39.folder_delete_all_files",
"url":6,
"doc":"Description: Deletes all the files of the given folder Args: fullPathOfTheFolder (str) : Location of the folder. extension (str) : extention of the file. by default all the files will be deleted inside the given folder regarless of the extension. Returns: [status] status (bool) - True if the file is deleted successfully.",
"func":1
},
{
"ref":"my_autopylot.folder39.folder_delete_file_or_folder",
"url":6,
"doc":"Description: Deletes single file or entire folder with all its contents. Args: file_or_folder_path (str) : Location of the file or folder. Returns: [status] status (bool) - True if the file is deleted successfully.",
"func":1
},
{
"ref":"my_autopylot.folder39.file_rename",
"url":6,
"doc":"Description: Renames the given file name to new file name with same extension Args: old_file_path (str) : Location of the file. new_file_name (str) : New file name. print_status (bool) : True if the status is to be printed. Returns: [status, data] status (bool) - True if the file is renamed successfully. data (List) - list of all the contents of the text file.",
"func":1
},
{
"ref":"my_autopylot.folder39.file_get_json_details",
"url":6,
"doc":"Description: Returns all the details of the given section in a dictionary Args: path_of_json_file (str) : Location of the json file. section (str) : section of the json file. Returns: [status, data] status (bool) - True if the file is renamed successfully. data - The contents of the JSON file.",
"func":1
},
{
"ref":"my_autopylot.keyboard39",
"url":7,
"doc":""
},
{
"ref":"my_autopylot.keyboard39.key_press",
"url":7,
"doc":"Description: Presses the given key / Emulates the given keystrokes on desired window. Args: key_1 (str, optional): Enter the 1st key Eg: ctrl or shift. Defaults to  . key_2 (str, optional): Enter the 2nd key in combination. Eg: alt or A. Defaults to  . key_3 (str, optional): Enter the 3rd key in combination. Eg: del or tab. Defaults to  . write_to_window (str, optional): (Only in Windows) Name of Window you want to activate. Defaults to  . Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.keyboard39.key_write_enter",
"url":7,
"doc":"Description: This function is used to write given text to a window and then press the enter/tab key. Args: text_to_write (str, optional): Text you wanted to type Eg: ClointFusion is awesone. Defaults to  . write_to_window (str, optional): (Only in Windows) Name of Window you want to activate Eg: Notepad. Defaults to  . key (str, optional): Press Enter key after typing. Eg: t for tab. Defaults to e Returns: [status] status (bool): True if successful, False if not.",
"func":1
},
{
"ref":"my_autopylot.keyboard39.key_hit_enter",
"url":7,
"doc":"Description: This function is used to press the enter key on a desired window. Args: write_to_window (str, optional): (Only in Windows)Name of Window you want to activate. Eg: Notepad. Defaults to  . Returns: [status] status (bool): True if successful, False if not.",
"func":1
},
{
"ref":"my_autopylot.mail39",
"url":8,
"doc":""
},
{
"ref":"my_autopylot.mail39.send_gmail_using_app_password",
"url":8,
"doc":"Description: Send email using Gmail from Desktop email application Args: gmail_username (str): [description]. Defaults to  . gmail_app_password (str): [description]. Defaults to  . to_email_id (str): [description]. Defaults to  . subject (str): [description]. Defaults to  . message (str): [description]. Defaults to  . attachment_path (optional): [description]. Defaults to  . Returns: [status] Status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.mail39.email_send_via_desktop_outlook",
"url":8,
"doc":"Description: Send email using Outlook from Desktop email application Args: to_email_id (str): [description]. Defaults to  . subject (str): [description]. Defaults to  . message (str): [description]. Defaults to  . attachment_path (str, optional): [description]. Defaults to  . Returns: [status] Status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.message39",
"url":9,
"doc":""
},
{
"ref":"my_autopylot.message39.msg_box_info",
"url":9,
"doc":"Description: Display a message box with information. Args: msg_for_user (str): [description] Returns: [status] Status (bool) : Whether the message box was displayed or not.",
"func":1
},
{
"ref":"my_autopylot.message39.msg_box_ask_yes_no",
"url":9,
"doc":"Description: Display a message box with information. Args: msg_for_user (str): [description] Returns: [status] Status (bool) : Whether the message box was displayed or not.",
"func":1
},
{
"ref":"my_autopylot.message39.msg_count_down",
"url":9,
"doc":"Description: Display a message box with information. Args: msg_for_user (str): [description] default_time (int, optional): [description]. Defaults to 5. Returns: [status] Status (bool) : Whether the message box was displayed or not.",
"func":1
},
{
"ref":"my_autopylot.mouse39",
"url":10,
"doc":""
},
{
"ref":"my_autopylot.mouse39.mouse_click",
"url":10,
"doc":"Description: Clicks at the given X Y Co-ordinates on the screen using single / double / triple click(s). Default clicks on current position. Args: x (int): x-coordinate on screen. Eg: 369 or 435, Defaults:  . y (int): y-coordinate on screen. Eg: 369 or 435, Defaults:  . left_or_right (str, optional): Which mouse button. Eg: right or left, Defaults: left. no_of_click (int, optional): Number of times specified mouse button to be clicked. Eg: 1 or 2, Max 3. Defaults: 1. Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.mouse39.mouse_move",
"url":10,
"doc":"Description: Moves the cursor to the given X Y Co-ordinates. Args: x (int): x-coordinate on screen. Eg: 369 or 435, Defaults:  . y (int): y-coordinate on screen. Eg: 369 or 435, Defaults:  . type_of_movement (str): Type of movement (Absolute or Relative to current Position). Eg: abs or rel, Defaults: abs. Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.mouse39.mouse_drag_from_to",
"url":10,
"doc":"Description: Clicks and drags from x1 y1 co-ordinates to x2 y2 Co-ordinates on the screen Args: x1 or x2 (int): x-coordinate on screen. Eg: 369 or 435, Defaults:  . y1 or y2 (int): y-coordinate on screen. Eg: 369 or 435, Defaults:  . delay (float, optional): Seconds to wait while performing action. Eg: 1 or 0.5, Defaults to 0.5. Returns: [status] status (bool): Whether the function is successful or failed.",
"func":1
},
{
"ref":"my_autopylot.mouse39.mouse_search_snip_return_coordinates_x_y",
"url":10,
"doc":"Description: Searches for the given image on the screen and returns the X and Y co-ordinates. Args: img (str): Image to search for. wait (int): Seconds to wait while performing action. Defaults to 10. Returns: [status, data] status: Whether the function is successful or failed. data: X and Y co-ordinates of the image.",
"func":1
},
{
"ref":"my_autopylot.pdf39",
"url":11,
"doc":""
},
{
"ref":"my_autopylot.pdf39.pdf_extract_all_tables",
"url":11,
"doc":"Description: Extract all tables from a pdf file and save them to a text file. Args: pdf_file_path (str): [description]. Defaults to  . output_folder (str): [description]. Defaults to  . output_file_name (str): [description]. Defaults to  . Returns: [status] status (bool) : Whether the pdf file was extracted or not.",
"func":1
},
{
"ref":"my_autopylot.pdf39.pdf_extract_table",
"url":11,
"doc":"Description: Extract a table from a pdf file and save it to a text file. Args: pdf_file_path (str): [description]. Defaults to  . table_number (int): [description]. Defaults to 0. page_number (int): [description]. Defaults to 0. output_folder (str): [description]. Defaults to  . output_file_name (str): [description]. Defaults to  . Returns: [status] status (bool) : Whether the pdf file was extracted or not.",
"func":1
},
{
"ref":"my_autopylot.screen_scraping39",
"url":12,
"doc":""
},
{
"ref":"my_autopylot.screen_scraping39.scrape_save_contents_to_notepad",
"url":12,
"doc":"Description: Copy pastes all the available text on the screen to notepad and saves it. Args: folderPathToSaveTheNotepad: Folder path to save the notepad file switch_to_window: Window name to switch to X: X coordinate of the screen to click and get focus Y: Y coordinate of the screen to click and get focus Returns: [status, data] status: True if successful, False if not data: Text copied from the screen by scraping",
"func":1
},
{
"ref":"my_autopylot.screen_scraping39.screen_clear_search",
"url":12,
"doc":"Description: Clears previously found text (crtl+f highlight) Args: delay: Delay in seconds. Default is 0.2 Returns: [status] status: True if successful, False if not",
"func":1
},
{
"ref":"my_autopylot.screen_scraping39.screen_scrape_extract_table",
"url":12,
"doc":"Description: Extracts the table from the screen and returns the data in a list. Args: switch_to_window (str, optional): [description]. Defaults to  . after_this_word (str, optional): [description]. Defaults to  . before_this_word (str, optional): [description]. Defaults to  . include_after_this_word (bool, optional): [description]. Defaults to False. include_before_this_word (bool, optional): [description]. Defaults to False. Returns: [status, data] status (bool): True if the function executed successfully. data (list): List of the data in the table.",
"func":1
},
{
"ref":"my_autopylot.string39",
"url":13,
"doc":""
},
{
"ref":"my_autopylot.string39.string_extract_only_alphabets",
"url":13,
"doc":"Description: Returns only alphabets from given input string Args: inputString: A string representing the name of the module to be installed. Returns: A boolean representing whether the module was installed successfully.",
"func":1
},
{
"ref":"my_autopylot.string39.string_extract_only_numbers",
"url":13,
"doc":"Description: Returns only numbers from given input string Args: inputString: A string representing the name of the module to be installed. Returns: A boolean representing whether the module was installed successfully.",
"func":1
},
{
"ref":"my_autopylot.string39.string_remove_special_characters",
"url":13,
"doc":"Description: Removes all the special character. Args: inputStr: A string representing the name of the module to be installed. Returns: Status - A boolean representing whether the module was installed successfully.",
"func":1
},
{
"ref":"my_autopylot.string39.string_extract_substring",
"url":13,
"doc":"Description: Extracts substring from a string. Args: string ([type]): [description] start_word ([type]): [description] end_word ([type]): [description] include_start_word (bool, optional): [description]. Defaults to False. include_end_word (bool, optional): [description]. Defaults to False. Returns: Status - Whether the substring was extracted or not.",
"func":1
},
{
"ref":"my_autopylot.utility39",
"url":14,
"doc":""
},
{
"ref":"my_autopylot.utility39.pause_program",
"url":14,
"doc":"Description: Stops the program for given seconds Args: seconds (str): seconds to be paused Returns: Status (bool) - True if success, False if failure",
"func":1
},
{
"ref":"my_autopylot.utility39.api_request",
"url":14,
"doc":"Description: Function used to send generic api request Args : url (str): url of the api method (str): method of the api request data (dict): data to be sent in the request headers (dict): headers to be sent in the request Returns : Status (bool) - True if success, False if failure",
"func":1
},
{
"ref":"my_autopylot.utility39.clipboard_set_data",
"url":14,
"doc":"Description: Set data to clipboard Args: data: data to be set to clipboard format_id: format of data Returns: Status (bool) - True if success, False if failure",
"func":1
},
{
"ref":"my_autopylot.utility39.GetClipboardFormats",
"url":14,
"doc":"",
"func":1
},
{
"ref":"my_autopylot.utility39.clipboard_get_data",
"url":14,
"doc":"Description: Get data from clipboard Returns: Status (bool) - True if success, False if failure",
"func":1
},
{
"ref":"my_autopylot.utility39.clear_output",
"url":14,
"doc":"Description: Clears Python Interpreter Terminal Window Screen Returns: Status (bool) - True if success, False if failure",
"func":1
},
{
"ref":"my_autopylot.utility39.install_module",
"url":14,
"doc":"",
"func":1
},
{
"ref":"my_autopylot.utility39.uninstall_module",
"url":14,
"doc":"",
"func":1
},
{
"ref":"my_autopylot.utility39.date_time_now",
"url":14,
"doc":"",
"func":1
},
{
"ref":"my_autopylot.utility39.add_datetime",
"url":14,
"doc":"",
"func":1
},
{
"ref":"my_autopylot.utility39.subtract_datetime",
"url":14,
"doc":"",
"func":1
},
{
"ref":"my_autopylot.utility39.image_to_text",
"url":14,
"doc":"",
"func":1
},
{
"ref":"my_autopylot.voice39",
"url":15,
"doc":""
},
{
"ref":"my_autopylot.voice39.playsound",
"url":15,
"doc":"Description: Play a sound file. Args: sound: A string containing the path to the sound file. block: A boolean indicating whether to block the program while the sound is playing. Returns: [status] status (bool): True if success, False otherwise.",
"func":1
},
{
"ref":"my_autopylot.voice39.speech_to_text",
"url":15,
"doc":"Description: Speech to Text using speech_recognition Args: None Returns: [status] status (bool): True if success, False otherwise. data (str): The text spoken.",
"func":1
},
{
"ref":"my_autopylot.voice39.text_to_speech",
"url":15,
"doc":"Description: Text to Speech using Google's Generic API Args: audio: A string containing the text to be spoken. show: A boolean indicating whether to show the text to be spoken. Returns: [status] status (bool): True if success, False otherwise.",
"func":1
},
{
"ref":"my_autopylot.windows39",
"url":16,
"doc":""
},
{
"ref":"my_autopylot.windows39.window_show_desktop",
"url":16,
"doc":"Description: Shows the desktop by minimizing all the windows. Args: None Returns: [staus] status (bool) : True if the window is found.",
"func":1
},
{
"ref":"my_autopylot.windows39.window_get_active_window",
"url":16,
"doc":"Description: Gives you the active window name. Args: None Returns: [status, data] status (bool) : True if the window is found. data (str) : Name/Title of the active window.",
"func":1
},
{
"ref":"my_autopylot.windows39.window_activate_window",
"url":16,
"doc":"Description: Activates the desired window. Args: window_title (str) : Name of the window to activate. Returns: [status] status (bool) : True if the window is found.",
"func":1
},
{
"ref":"my_autopylot.windows39.window_get_all_opened_titles_windows",
"url":16,
"doc":"Description: Gives the title of all the existing (open) windows. Args: None Returns: [status, data] status (bool) : True if the window is found. data (list) : List of all the opened windows.",
"func":1
},
{
"ref":"my_autopylot.windows39.window_activate_and_maximize_windows",
"url":16,
"doc":"Description: Activates and maximizes the desired window. Args: windowName (str) : Name of the window to maximize. Returns: [status] status (bool) : True if the window is found.",
"func":1
},
{
"ref":"my_autopylot.windows39.window_minimize_windows",
"url":16,
"doc":"Description: Activates and minimizes the desired window. Args: windowName (str) : Name of the window to miniimize. Returns: [status] status (bool) : True if the window is found.",
"func":1
},
{
"ref":"my_autopylot.windows39.window_close_windows",
"url":16,
"doc":"Description: Close the desired window. Args: windowName (str) : Name of the window to close. Returns: [status] status (bool) : True if the window is found.",
"func":1
},
{
"ref":"my_autopylot.windows39.launch_any_exe_bat_application",
"url":16,
"doc":"Description: Launches any exe or batch file or excel file etc. Args: pathOfExeFile (str, optional): Location of the file with extension Eg: Notepad, TextEdit. Defaults to  . Returns: [status] Status (bool) : True if the file is found.",
"func":1
},
{
"ref":"my_autopylot.windows39.window_restore_windows",
"url":16,
"doc":"Description: Restores the desired window. Args: windowName (str) : Name of the window to restore. Returns: [status] Status (bool) : True if the window is found.",
"func":1
}
]