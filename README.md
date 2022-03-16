## Welcome to Auto-Pylot , Made in India with &#10084;&#65039; 

<br>

<img src="https://raw.githubusercontent.com/py-bots/media-pyles/main/autopylot/Auto%20Pylot%20Figlet%20Dark.png">


# What is Auto-Pylot?

PyBots is an Indian firm based in Vadodara, Gujarat. Auto-Pylot is a product developed based on Python. Its a RPA framework for developers and common people to create Software BOTs. Using AI, we're working on Common Man's RPA.


<!-- #### Check out Project Status

![PyPI](https://img.shields.io/pypi/v/ClointFusion?label=PyPI%20Version) 
![PyPI - License](https://img.shields.io/pypi/l/ClointFusion?label=License) 
![PyPI - Status](https://img.shields.io/pypi/status/ClointFusion?label=Release%20Status) 
![ClointFusion](https://snyk.io/advisor/python/ClointFusion/badge.svg) 
![PyPI - Downloads](https://img.shields.io/pypi/dm/ClointFusion?label=PyPI%20Downloads) 
![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/ClointFusion) 
![PyPI - Format](https://img.shields.io/pypi/format/ClointFusion?label=PyPI%20Format) 
![GitHub contributors](https://img.shields.io/github/contributors/ClointFusion/ClointFusion?label=Contributors) 
![GitHub last commit](https://img.shields.io/github/last-commit/ClointFusion/ClointFusion?label=Last%20Commit) 

![GitHub Repo stars](https://img.shields.io/github/stars/ClointFusion/ClointFusion?label=Stars&style=social) 
![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FClointFusion) 
![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCIygBtp1y_XEnC71znWEW2w?style=social) 
![Twitter Follow](https://img.shields.io/twitter/follow/ClointFusion?style=social) -->
<!-- 
## Release Notes

- Click here for <a href="https://github.com/ClointFusion/ClointFusion/blob/master/Release_Notes.txt" target="_blank"> Release Notes</a>

--- -->

# Installation

<br>

> ### Auto-Pylot is currently supported on Windows only ! (For macOS and Linux : Comming soon.)

## Windows :

* Auto-Pylot is compatible with both Windows 10 and Windows 11.
* Installing on a Windows PC is a breeze.
* Make certain that Python 3.8 or Python 3.9 is installed.
* Then, from the command prompt, execute the following command.

    ```
    pip install -U auto-pylot
    ```

# Importing

<br>

> ### Auto-Pylot can be accessed using one of two methods.

## Windows :

* ### Terminal : Opens a Python interpreter using the command " import auto-pylot as ap "

    ```
    ap_py
    ```
* ### Code Editor or IDE : Import Auto-Pylot first, and then run the file in Python.

    ```
    # ap_bot.py

    import auto-pylot as cf

    ap.windows_launch_app('notepad')
    ```
    ```
    python ap_bot.py
    ```


# Auto-Pylot in Action

## **Now access more than 100 functions (hit ctrl+space in your IDE)**

***TIP: You can find and inspect all of Auto-Pylot's functions using only one function i.e., `find()`. Just pass the partial name of the function.***

```
ap.find("sort")

ap.find("gui")

```

* ### 4 functions on Mouse Operations:

| Function | Accepted Parameters | Description |
| :--------: | :----: | :----------- |
| ap.mouse_click() | x=" ", y=" ", left_or_right="left", no_of_clicks=1, type_of_movement="abs or rel"  | Clicks at the given X Y Co-ordinates on the screen using ingle / double / triple click(s). Optionally copies selected data to clipboard (works for double / triple clicks) |
| ap.mouse_move() | x=" ", y=" ", type_of_movement="abs or rel" | Moves the cursor to the given X Y Co-ordinates |
| ap.mouse_drag_from_to() | x1=" ", y1=" ", x2=" ",y2=" " | Clicks and drags from X1 Y1 co-ordinates to X2 Y2 Co-ordinates on the screen |
| ap.mouse_search_snip_return_coordinates_x_y() | img=" ", wait=10 | Searches the given image on the screen and returns its center of X Y co-ordinates. |

<br>
<!-- <img src="https://github.com/ClointFusion/Image_ICONS_GIFs/blob/main/Mouse_Operations.gif?raw=true" height="400"> -->

----

* ### 8 functions on Window Operations (works only in Windows OS):

| Function | Accepted Parameters | Description |
| :--------: | :----: | :----------- |
| ap.windows_show_desktop() | None | Minimizes all the applications and shows Desktop. |
| ap.windows_launch_app() | pathOfExeFile=" " | Launches any exe or batch file or excel file etc. |
| ap.window_get_active_window() | None | Launches any exe or batch file or excel file etc. |
| ap.window_activate_window() | window_title=" " | Launches any exe or batch file or excel file etc. |
| ap.window_get_all_opened_titles_windows() | window_title=" " | Gives the title of all the existing (open) windows. |
| ap.window_activate_and_maximize_windows() | windowName=" " | Activates and maximizes the desired window. |
| ap.window_minimize_windows() | windowName=" " | Activates and minimizes the desired window. | 
| ap.window_close_windows() | windowName=" " | Close the desired window. |

<br>
<!-- <img src="https://github.com/ClointFusion/Image_ICONS_GIFs/blob/main/Functions%20Light%20GIFs/Window Operations.gif?raw=true" height="400"> -->

----

* ### 8 functions on Folder Operations:

| Function | Accepted Parameters | Description |
| :--------: | :----: | :----------- |
| ap.folder_read_text_file() | txt_file_path=" " | Reads from a given text file and returns entire contents as a single list |
| ap.folder_write_text_file() | txt_file_path=" ", contents=" " |  Writes given contents to a text file |
| ap.folder_create() | strFolderPath=" " | When you are making leaf directory, if any intermediate-level directory is missing, folder_create() method creates them. |
| ap.folder_create_text_file() | textFolderPath=" ", txtFileName=" " | Creates text file in the given path. |
| ap.folder_get_all_filenames_as_list() | strFolderPath=" ", extension='all' | Get all the files of the given folder in a list. |
| ap.folder_delete_all_files() | fullPathOfTheFolder=" ", file_extension_without_dot="all" | Deletes all the files of the given folder |
| ap.file_rename() | old_file_path='', new_file_name='', print_status=True | Renames the given file name to new file name with same extension. |
| ap.file_get_json_details() | path_of_json_file='', section='' | Returns all the details of the given section in a dictionary |

<br>
<!-- <img src="https://github.com/ClointFusion/Image_ICONS_GIFs/blob/main/Folder_Operations.gif?raw=true" height="400"> -->

----

* ### 3 functions on Keyboard Operations:

| Function | Accepted Parameters | Description |
| :--------: | :----: | :----------- |
| ap.key_press() | key_1='', key_2='', key_3='', write_to_window=" " | Emulates the given keystrokes. |
| ap.key_write_enter() | text_to_write=" ", write_to_window=" ", delay_after_typing=1, key="e" | Writes/Types the given text and press enter (by default) or tab key. |
| ap.key_hit_enter() | write_to_window=" " | Enter key will be pressed once. |

<br>
<!-- <img src="https://github.com/ClointFusion/Image_ICONS_GIFs/blob/main/KB_Operations.gif?raw=true" height="400"> -->

----

* ### 5 functions on Screen-scraping Operations:

| Function | Accepted Parameters | Description |
| :--------: | :----: | :----------- |
| ap.scrape_save_contents_to_notepad() | folderPathToSaveTheNotepad=" ", switch_to_window=" ",X=0, Y=0 | Copy pastes all the available text on the screen to notepad and saves it. |
| ap.screen_clear_search() | delay=0.2 | Clears previously found text (crtl+f highlight) |
| ap.search_highlight_tab_enter_open() | searchText=" ", hitEnterKey="Yes", shift_tab='No' | Searches for a text on screen using crtl+f and hits enter. This function is useful in Citrix environment. |
| ap.find_text_on_screen() | searchText=" ", delay=0.1, occurance=1, isSearchToBeCleared=False | Clears previous search and finds the provided text on screen. |

<br>
<!-- <img src="https://github.com/ClointFusion/Image_ICONS_GIFs/blob/main/Screen_Scraping.gif?raw=true" height="400"> -->

----

* ### 11 functions on Browser Operations:

| Function | Accepted Parameters | Description |
| :--------: | :----: | :----------- |
| driver = ap.ChromeBrowser() |  | Function to launch browser and start the session. |
| driver.open_browser() | dummy_browser=True,<br> incognito=False,<br> profile="Default" | Function to launch browser and start the session. |
| driver.navigate() | url=" " | Navigates to Specified URL. |
| driver.write() | Value=" ",  User_Visible_Text_Element=" " |  Write a string on the given element. |
| driver.mouse_click() | User_Visible_Text_Element=" ", element=" ",<br> double_click=False, right_click=False | Click on the given element. |
| driver.mouse_hover() | User_Visible_Text_Element=" " | Performs a Mouse Hover over the Given User Visible Text Element |
| driver.scroll() | direction="down", weight="100" px  | Scrolls the browser window. | 
| driver.key_press() | key_1=" ", key_2=" " | Type text using Browser Helium Functions and press hot keys |
| driver.hit_enter() | None | Hits enter KEY using Browser Helium Functions |
| driver.wait_until() | text=" ", element="t" | Wait until a specific element is found. |
| driver.refresh_page() | None | Refresh the page. |
| driver.set_waiting_time() | time=10 | Set the waiting time for the self.browser_driver. If element is not found in the given time, it will raise an exception.
| driver.find_element() | element_xpath="xpath" | Find the element using xpath.
| driver.get_text() | element_xpath=" ", element="t" | Wait until a specific element is found. |
| driver.close() | None | Close the Helium browser. |

<br>
<!-- <img src="https://github.com/ClointFusion/Image_ICONS_GIFs/blob/main/Functions%20Light%20GIFs/browser_functions.gif?raw=true" height="400"> -->

----
<!-- 
* ### 4 functions on Alert Messages:

| Function | Accepted Parameters | Description |
| :--------: | :----: | :----------- |
| ap.message_counter_down_timer() | strMsg="Calling ClointFusion Function in (seconds)", start_value=5 | Function to show count-down timer. Default is 5 seconds. |
| ap.message_pop_up() | strMsg=" ", delay=3 | Specified message will popup on the screen for a specified duration of time.|
| ap.message_flash() | msg=" ", delay=3 | Specified msg will popup for a specified duration of time with OK button. |
| ap.message_toast() | message,website_url=" ", file_folder_path=" " | Function for displaying Windows 10 Toast Notifications. Pass website URL OR file / folder path that needs to be opened when user clicks on the toast notification. |

---- -->

* ### 3 functions on String Operations: 

| Function | Accepted Parameters | Description |
| :--------: | :----: | :----------- |
| ap.string_remove_special_characters() | inputStr=" " | Removes all the special character. |
| ap.string_extract_only_alphabets() | inputString=" " | Returns only alphabets from given input string |
| ap.string_extract_only_numbers() | inputString=" " | Returns only numbers from given input string |

<br>
<!-- <img src="https://github.com/ClointFusion/Image_ICONS_GIFs/blob/main/String_Operations.gif?raw=true" height="400"> -->

----

* ### Loads of miscellaneous functions related to emoji, capture photo, flash (pop-up) messages etc:

| Function | Accepted Parameters | Description |
| :--------: | :----: | :----------- |
| ap.clear_screen() | None | Clears Python Interpreter Terminal Window Screen |
| ap.print_with_magic_color() | strMsg:str=" ", magic:bool=False | Function to color and format terminal output |
| ap.show_emoji() | strInput=" " | Function which prints Emojis |
| ap.download_this_file() | url=" " | Downloads a given url file to BOT output folder or Browser's Download folder |
| ap.pause_program() | seconds="5" | Stops the program for given seconds |

<br>
<!-- <img src="https://github.com/ClointFusion/Image_ICONS_GIFs/blob/main/miscallaneous.gif?raw=true" height="400">     -->


<!-- # BOTS made out of Auto-Pylot

### Outlook Email BOT implemented using Auto Pylot

<img src="https://github.com/ClointFusion/Image_ICONS_GIFs/blob/main/Functions%20Light%20GIFs/Gmail_and_Outlook_BOT.gif?raw=true" height="400">

<br> -->

# We love your contribution

Contribute to us by giving a star, writing articles on `Auto-Pylot`, giving comments, reporting bugs, bug fixes, feature enhancements, adding documentation, and many other ways. 


## Invitation to our Monthly Branded Hackathon

We also invite everyone to take part in our monthly branded event, the `Auto-Pylot Hackathon`, and stand a chance to work with us.

<!-- Checkout our Hackathon Website for more details here: [ClointFusion Hackathon](https://sites.google.com/view/clointfusion-hackathon -->
<!-- ) -->

<br>

## Date &#10084;&#65039; with Auto-Pylot

<!-- This an initiative for fast track entry into our growing workforce. For more details, please visit: [Date with ClointFusion](https://lnkd.in/gh_r9YB) -->


## Acknowledgements

We sincerely thanks to all it's dependent packages for the great contribution, which made `Auto-Pylot` possible!

<!-- Please find all the dependencies [here](https://openbase.com/python/ClointFusion/dependencies)  -->
<!-- 
<a href="https://openbase.com/python/ClointFusion/dependencies" target="blank">ClointFusion thanks all its dependent packages for the great contribution, which has made ClointFusion possible !</a> -->


## Need help in Building BOTS?

Write us by clicking below<br>
<div align='left'>
<a href="mailto:support@pybots.ai" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"></a> &nbsp;
</div>

---

<!-- Disclaimer: We collect anonymous data on installation and usage statistics in order to improve our product and provide better services. -->