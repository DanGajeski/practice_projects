import argparse
import json
import os
import time
from datetime import datetime
from pathlib import Path
from xml.etree.cElementTree import TreeBuilder

from PIL import Image

# JESUS IS LORD

# picture_store = {"pictureIndex": []}

# initial_input = ""

# if initial_input == "add":
#     pass
# elif initial_input == "annotate":
#     pass
# elif initial_input == "search":
#     pass


class Picture_indexer:
    def __init__(self):

        # self.passed_args = args

        # self.wow_screenshots_folder = Path(
        #     "C:/Program Files (x86)/World of Warcraft/_retail_/Screenshots"
        # )
        # self.wow_test_screenshots_folder = Path(
        #     "C:/Users/Zen/Desktop/example_screenshots/WOW"
        # )
        # self.twwh_screenshots_folder = Path(
        #     "C:/Program Files (x86)/Steam/userdata/109185688/760/remote/1142710/screenshots"
        # )
        # self.twwh_test_screenshots_folder = Path(
        #     "C:/Users/Zen/Desktop/example_screenshots/TWWH"
        # )
        # self.bg3_screenshots_folder = Path(
        #     "C:/Program Files (x86)/Steam/userdata/109185688/760/remote/1086940/screenshots"
        # )
        # self.bg3_test_screenshots_folder = Path(
        #     "C:/Users/Zen/Desktop/example_screenshots/BG3"
        # )
        # self.wow_game_id = "wow"
        # self.twwh_game_id = "twwh"
        # self.bg3_game_id = "bg3"
        self.main_dict = {"pictureIndex": []}
        self.main_dict_file_location = ""
        # self.screenshot_folders_and_game_ids = {
        #    self.wow_screenshots_folder: self.wow_game_id,
        #    self.twwh_screenshots_folder: self.twwh_game_id,
        #    self.bg3_screenshots_folder: self.bg3_game_id,
        # }  # combine for add_entries_to_main_dict function

        self.screenshot_folders_and_game_ids = {}  # LOADS paths and path game ids FROM config file (picture_indexer_config.json)

        self.working_requested_entries = []  # list for containing working set of requested entries from user
        self.requested_entries = []  # finalized list containing requested user entries by game name and date
        self.user_supplied_date_range = [
            "2023-08-08",
            "2023-11-13",
        ]  ### TEST/HARDCODED user supplied date range in yyyy-mm-dd format
        self.user_supplied_beginning_date = {
            "supplied": False,
            "date": "",
        }  # for user's beginning date.  separated from end date
        self.user_supplied_end_date = {
            "supplied": False,
            "date": "",
        }  # for user's end date.  separated from beginning date
        self.user_supplied_game_id = (
            "wow"  ### TEST/HARDCODED user supplied game id in string format
        )
        self.unprocessed_user_input = ""
        self.running = (
            True  # bool for main loop running check // False if user quits program
        )
        self.user_input_game_id = ""
        self.user_input_init_date = ""
        self.user_input_end_date = ""
        self.user_selected_screenshot = ""
        self.user_annotation = ""

        self.game_details = {"games": []}

        self.args = argparse.Namespace  # TESTING, INITIALLY UNFILLED ARGPARSE.NAMESPACE

        self.args_present = False  # Tracking if args are passed into the program or not

        # print(self.main_dict)
        self._load_config_file()
        # print(self.main_dict)
        self._setup_screenshots_folders_and_game_ids_var()
        # print(self.main_dict)

        # print(self.main_dict)
        self._load_files_from_json_test()  # OPTIONS FOR BOTH INTERACTIVE AND NON INTERACTIVE MODE, LOADS SCREENSHOT FOLDER INFORMATION INTO self.main_dict
        # print(self.main_dict)

        self.args_present = self.parse_args()  # check for if args are passed in.  if args passed in run non-interactive program with passed in args.  if no args present run interactive input

    def parse_args(self):
        parser = argparse.ArgumentParser(
            description="A Test for argparse in picture indexer"
        )
        # parser.add_argument("--theta", action="store")
        parser.add_argument(
            "--game", action="store", help="Selects game to search for."
        )
        parser.add_argument(
            "--before", action="store", help="Selects initial date to search for."
        )
        parser.add_argument(
            "--after", action="store", help="Selects end date to search for."
        )
        parser.add_argument(
            "--annotate",
            action="store",
            nargs=2,
            metavar=("screenshot_id", "annotation_string"),
            help="Annotate selected screenshot",
        )
        parser.add_argument(
            "--saveall", action="store", help="Saves selections and annotations"
        )
        parser.add_argument(
            "--deleteall",
            action="store_true",
            help="Deletes selections and annotations",
        )

        args = parser.parse_args()

        args_present = (
            False  # RETURN value to let program know if args were passed in or not
        )

        self.user_supplied_beginning_date = {
            "supplied": False,
            "date": "",
        }  # for user's beginning date.  separated from end date
        self.user_supplied_end_date = {
            "supplied": False,
            "date": "",
        }  # for user's end date.  separated from beginning date
        self.user_supplied_game_id = (
            "wow"  ### TEST/HARDCODED user supplied game id in string format
        )
        # self.user_input_game_id

        if args.game:
            self.user_input_game_id = args.game
            self.get_dict_entries_by_game_id()  # GAME ID SPECIFIED IN COMMAND LINE
            args_present = True
            if args.before and args.after:
                print(f"AFTER {args.after}, BEFORE {args.before}.")
                self.user_supplied_beginning_date["supplied"] = True
                self.user_supplied_beginning_date["date"] = args.after  # end date
                self.user_supplied_end_date["supplied"] = True
                self.user_supplied_end_date["date"] = args.before  # beginning date
                self.get_dict_entries_by_date_range()
                args_present = True
                self.save_main_dict_to_json()
            if args.after:
                print(f"ONLY AFTER {args.after}.")
                self.user_supplied_beginning_date["supplied"] = True
                self.user_supplied_beginning_date["date"] = args.after
                self.get_dict_entries_by_date_range()
                args_present = True
                self.save_main_dict_to_json()

            if args.before:
                print(f"ONLY BEFORE {args.before}.")
                self.user_supplied_end_date["supplied"] = True
                self.user_supplied_end_date["date"] = args.before
                self.get_dict_entries_by_date_range()
                args_present = True
                self.save_main_dict_to_json()

        else:
            #     self.get_dict_entries_if_no_game_id_specified()  # NO GAME ID SPECIFIED IN COMMAND LINE

            if args.before and args.after:
                self.get_dict_entries_if_no_game_id_specified()
                print(f"AFTER {args.after}, BEFORE {args.before}.")
                self.user_supplied_beginning_date["supplied"] = True
                self.user_supplied_beginning_date["date"] = args.after  # end date
                self.user_supplied_end_date["supplied"] = True
                self.user_supplied_end_date["date"] = args.before  # beginning date
                self.get_dict_entries_by_date_range()
                args_present = True
                self.save_main_dict_to_json()

            elif args.after:
                self.get_dict_entries_if_no_game_id_specified()
                print(f"ONLY AFTER {args.after}.")
                self.user_supplied_beginning_date["supplied"] = True
                self.user_supplied_beginning_date["date"] = args.after
                self.get_dict_entries_by_date_range()
                args_present = True
                self.save_main_dict_to_json()

            elif args.before:
                self.get_dict_entries_if_no_game_id_specified()
                print(f"ONLY BEFORE {args.before}.")
                self.user_supplied_end_date["supplied"] = True
                self.user_supplied_end_date["date"] = args.before
                self.get_dict_entries_by_date_range()
                args_present = True
                self.save_main_dict_to_json()

        self.sort_dict_by_game_and_date()  # takes in self.main_dict["pictureIndex"] and replaces values with all contents SORTED by DATE and GAME
        self._display_selected_screenshots()

        if args.deleteall:
            print(f"DELETING SELECTIONS AND ANNOTATIONS FROM JSON")
            # NEED FUNCTION TO DELETE ALL ADDED VALUES FROM self.main_dict["pictureIndex"]
            self._delete_all_selected_files()  # resets to false "game_requested" and "date_reqeusted" entry values, deletes json file containing main_dict

            print(self.main_dict_file_location)
            if os.path.exists(self.main_dict_file_location):
                os.remove(self.main_dict_file_location)
                print("DELETING MAIN DICT FILE LOCATION JSON")
            else:
                print("MAIN DICT FILE LOCATION DOES NOT EXIST")

            args_present = True
        if args.saveall:
            print(f"SAVING SELECTIONS AND ANNOTATIONS TO JSON")
            # self._save_selected_files_to_json_test()
            self.save_main_dict_to_json()
            print("SAVING non interactive DATA TO JSON")
            args_present = True

        if args.annotate:
            print("ANNOTATING")

            # parser.add_argument(
            #     "--annotate",
            #     action="store",
            #     nargs=2,
            #     metavar=("screenshot_id", "annotation_string"),
            #     help="Annotate selected screenshot",
            # )
            screenshot_id, annotation_string = args.annotate

            for entry in self.main_dict["pictureIndex"]:
                if entry["screenshot_id"] == screenshot_id:
                    entry["annotation"] = annotation_string

            args_present = True
            self.save_main_dict_to_json()

            # def _save_selected_files_to_json(self):
        # self.convert_main_dict_paths_to_strings()  # SAVE ANNOTATIONS TO JSON
        # with open("main_dict.json", "w") as file:
        #     json.dump(self.main_dict, file, indent=4)
        # self.save_main_dict_to_json()

        # for entry in self.main_dict["pictureIndex"]:
        #     if entry["screenshot_id"] == self.user_selected_screenshot:
        #         entry["annotation"] = self.user_annotation
        #         print("ADDING ANNOTATION")

        # if args.annotation:

        return args_present

    def save_main_dict_to_json(self):
        self.convert_main_dict_paths_to_strings()
        with open("main_dict.json", "w") as file:
            json.dump(self.main_dict, file, indent=4)

    def _delete_all_selected_files(self):
        print("REMOVING GAMEREQUESTED AND DATEREQUESTED")
        for entry in self.main_dict["pictureIndex"]:
            if entry["game_requested"]:
                # print("REMOVING ENTRY")
                entry["game_requested"] = False
            if entry["date_requested"]:
                # print("REMOVING ENTRY")
                entry["date_requested"] = False
            # print("REMOVING ENTRY")

        for entry in self.main_dict["pictureIndex"]:
            if entry["game_requested"]:
                print("GAME REQUESTED STILL THERE")

        # for entry in self.main_dict["pictureIndex"]:
        #     # print(entry)
        #     if (
        #         entry["game_requested"]
        #         and entry[
        #             "date_requested"

    def _save_selected_files_to_json_test(self):
        self.convert_main_dict_paths_to_strings()
        with open("main_dict.json", "w") as file:
            json.dump(self.main_dict, file, indent=4)

    def _load_files_from_json_test(self):
        try:
            with open("main_dict.json", "r") as file:
                # print(self.main_dict)
                print("THERE IS A MAIN DICT LOADING HERE")
                self.main_dict = json.load(file)
                self.convert_main_dict_strings_to_paths()
                print("LOADING FILES FROM JSON")
                # print(self.main_dict)
        except:
            # print(self.main_dict)
            self.run_picture_indexer_setup()
            for entry in self.main_dict["pictureIndex"]:
                if entry["game_requested"]:
                    print("GAME FUCKING REQUESTED")
            # print(self.main_dict)
            print("INITIALIZING FRESHLY PULLED SCREENSHOT FILES")

    def run_picture_indexer_setup(self):
        self.add_entries_to_main_dict_picture_index()  # adds screenshots from wow, twwh, and bg3 to main_dict

    def _load_config_file(self):
        with open("picture_indexer_config.json", "r") as file:
            config_dict = json.load(file)
            for entry in config_dict[
                "games"
            ]:  # pulls entries from json config into self.game_details["games"]
                self.game_details["games"].append(entry)
            for entry in self.game_details[
                "games"
            ]:  # sets screenshotsFolder path into a WindowsPath() object
                entry["screenshotsFolder"] = Path(entry["screenshotsFolder"])
            if self.main_dict_file_location == "":
                self.main_dict_file_location = config_dict[
                    "main_dict_file_location"
                ]  # get's value of confic_dict["main_dict_file_location"]
                print("ADDING MAINDICTFILELOCATION!!!!")

    def _setup_screenshots_folders_and_game_ids_var(
        self,
    ):  # fills self.main_dict["pictureIndex"] list with entries in folders provided by picture_indexer_config.json
        for entry in self.game_details["games"]:
            self.screenshot_folders_and_game_ids[entry["screenshotsFolder"]] = entry[
                "id"
            ]

    def run_picture_indexer_main_loop(self):  # BEGINS INTERACTIVE MODE
        print(self.args_present)
        if not (
            self.args_present
        ):  # ONLY RUN INTERACTIVE VERSION OF PROGRAM IF NO ARGS PRESENT
            while self.running:
                self.print_intro()
                self.get_unprocessed_user_input()
            if not self.running:
                self.print_outro()

    def print_intro(self):
        print("Thank you for using the picture index program")

    def print_outro(self):
        print(
            "Saving Selected Screenshots... Thank you for using the picture index program."
        )

    def _end_main_loop(self):
        self.running = False

    def _display_all_screenshots(self):
        for entry in self.main_dict["pictureIndex"]:
            # print(entry)
            if entry["annotation"] == "":
                print(
                    f"Filename: {entry['name']}, Creation date: {entry['created']}, Game id: {entry['game_id']}, Screenshot id: {entry['screenshot_id']}"
                )
            else:
                print(
                    f"Filename: {entry['name']}, Creation date: {entry['created']}, Game id: {entry['game_id']}, Screenshot id: {entry['screenshot_id']}, Annotation: {entry['annotation']}"
                )

    def _display_selected_screenshots(self):  # displays currently selected screenshots
        # for entry in self.requested_entries:
        # self._delete_all_selected_files()
        date_selected_from_pictureIndex = self.check_if_dates_selected()
        for entry in self.main_dict["pictureIndex"]:
            if (
                entry["game_requested"]
                and entry[
                    "date_requested"
                ]  # DISPLAY SCREENSHOTS WHEN BOTH GAME REQUESTED AND DATE REQUESTED
            ):  # if BOTH game_requested and date_requested, print selected value
                if entry["annotation"] == "":
                    print(
                        f"Filename: {entry['name']}, Creation date: {entry['created']}, Game id: {entry['game_id']}, Screenshot id: {entry['screenshot_id']}"
                    )
                else:
                    print(
                        f"Filename: {entry['name']}, Creation date: {entry['created']}, Game id: {entry['game_id']}, Screenshot id: {entry['screenshot_id']}, Annotation: {entry['annotation']}"
                    )
            elif (
                entry["game_requested"]
                and not date_selected_from_pictureIndex  # DISPLAY SCREENSHOTS WHEN ONLY GAME SELECTED AND NO DATE SELECTED IN ALL OF THE ENTRIES
            ):  # if ONLY game requested and NO date selection in ANY of the entries
                # print(entry["game_requested"])
                # print(date_selected_from_pictureIndex)

                if entry["annotation"] == "":
                    print(
                        f"Filename: {entry['name']}, Creation date: {entry['created']}, Game id: {entry['game_id']}, Screenshot id: {entry['screenshot_id']}"
                    )
                else:
                    print(
                        f"Filename: {entry['name']}, Creation date: {entry['created']}, Game id: {entry['game_id']}, Screenshot id: {entry['screenshot_id']}, Annotation: {entry['annotation']}"
                    )
                # entry["game_requested"] = False
                # print(entry["game_requested"])
                # print("END PRINTING PHANTOM ENTRY")

    def check_if_dates_selected(
        self,
    ) -> bool:  # RETURNS FALSE if NO dates selected in ALL entries, RETURNS TRUE if entry['date_requested'] values are found (meaning entry selected via date) in ANY entry
        date_selected_found = False

        for entry in self.main_dict["pictureIndex"]:
            if entry["date_requested"]:
                date_selected_found = True
                print("DATE SELECTED FOUND")

        return date_selected_found

    def convert_main_dict_paths_to_strings(
        self,
    ):  # convert self.main_dict["pictureIndex"] ["path"] entries from Path(s) to strings
        for entry in self.main_dict["pictureIndex"]:
            entry["path"] = str(entry["path"])

    def convert_main_dict_strings_to_paths(
        self,
    ):  # convert self.main_dict["pictureIndex"] ["path"] entries from strings to Path(s)
        for entry in self.main_dict["pictureIndex"]:
            entry["path"] = Path(entry["path"])

    def _save_selected_files_to_json(self):
        self.convert_main_dict_paths_to_strings()
        with open("main_dict.json", "w") as file:
            json.dump(self.main_dict, file, indent=4)

    # def _load_files_from_json_test(
    #     self,
    # ):
    #     try:
    #         with open("main_dict.json", "r") as file:
    #             self.main_dict = json.load(file)
    #             self.convert_main_dict_strings_to_paths()
    #             print("LOADING FILES FROM JSON INTERACTIVELY")
    #     except:
    #         self.run_picture_indexer_setup()
    #         print("INITIALIZING FRESHLY PULLED SCREENSHOT FILES INTERACTIVELY")

    def _load_files_from_json(
        self,
    ):  # ONLY LOADS FILES FROM JSON IF IN INTERACTIVE MODE.  ELSE RUNS PICTURE INDEXER SETUP WHICH LOADS SCREENSHOTS FOLDERS CONTENTS INTO MAIN_DICT
        if not self.args_present:  # ONLY USE SELECTED JSON FILE IF IN INTERACTIVE MODE
            try:
                with open("main_dict.json", "r") as file:
                    self.main_dict = json.load(file)
                    self.convert_main_dict_strings_to_paths()
                    print("LOADING FILES FROM JSON INTERACTIVELY")
            except:
                self.run_picture_indexer_setup()
                print("INITIALIZING FRESHLY PULLED SCREENSHOT FILES INTERACTIVELY")
        else:  # RUNNING PICTURE INDEXER SETUP TO ADD FILES TO MAIN_DICT
            print("INITIALIZING FRESHLY PULLED SCREENSHOT FILES NON INTERACTIVELY")
            self.run_picture_indexer_setup()

    def _select_screenshots_by_game_and_date(self):
        # self.user_input_game_id = ""
        # self.user_supplied_beginning_date["date"] = ""
        # self.user_supplied_beginning_date["supplied"] = False
        # self.user_supplied_end_date["date"] = ""
        # self.user_supplied_end_date["supplied"] = False

        self.user_input_game_id = input(
            "Please input a game_id to select from (Leave blank to select from all games): "
        )
        self.user_supplied_beginning_date["date"] = input(
            "Please input an initial date to select from (format: yyyy-mm-dd, leave blank if no beginning date): "
        )
        if self.user_supplied_beginning_date["date"] != "":
            self.user_supplied_beginning_date["supplied"] = True
        self.user_supplied_end_date["date"] = input(
            "Please input an end date to select from (format: yyyy-mm-dd, leave blank if no end date): "
        )
        if self.user_supplied_end_date["date"] != "":
            self.user_supplied_end_date["supplied"] = True
        print(
            "Your selections have been saved.  Please select 'Display selected screenshots' to view your selections"
        )
        if self.user_input_game_id == "":
            self.get_dict_entries_if_no_game_id_specified()  # fill self.working_requested_entries with all games
        elif self.user_input_game_id != "":
            self.get_dict_entries_by_game_id()  # fill self.working_requested_entries with only games by selected id
        self.get_dict_entries_by_date_range()  # TEST to fill requested entries by ONLY beginning date, ONLY end date, or BOTH

    def _select_and_annotate_screenshot(self):
        self.user_selected_screenshot = input(
            "Please input a screenshot id of an item that you would like to annotate: "
        )
        self.user_annotation = input(
            "Please add the text that you wish to annotate the screenshot with: "
        )
        for entry in self.main_dict["pictureIndex"]:
            if entry["screenshot_id"] == self.user_selected_screenshot:
                entry["annotation"] = self.user_annotation
                print("ADDING ANNOTATION")

    def _select_and_display_screenshot_in_default_app(self):
        self.user_selected_screenshot = input(
            "Please input a screenshot id of an item that you would like to view: "
        )

        for entry in self.main_dict["pictureIndex"]:
            if entry["screenshot_id"] == self.user_selected_screenshot:
                os.startfile(
                    rf"{str(entry['path'])}"
                )  # diplays selected screenshot via path in windows default app

    def _reset_requested_entries(
        self,
    ):  # in self.main_dict["pictureIndex"] list, in every dict in the list, keys ["game_requested"] and ["date_requested"] bool values are reset to FALSE
        # ALSO resets self variables used for tracking user supplied information gathered from interactive command line
        for entry in self.main_dict["pictureIndex"]:
            if entry[
                "game_requested"
            ]:  # evaulates to if entry["game_requested"] == True.   ### swaps to False if True
                entry["game_requested"] = False
            if entry[
                "date_requested"
            ]:  # evaluates to if entry["date_requested"] == True.   ### swaps to False if True
                entry["date_requested"] = False

        self.user_input_game_id = ""
        self.user_supplied_beginning_date["date"] = ""
        self.user_supplied_beginning_date["supplied"] = False
        self.user_supplied_end_date["date"] = ""
        self.user_supplied_end_date["supplied"] = False

    def get_unprocessed_user_input(
        self,
    ):  # for INTERACTIVE mode, gets user input and decides what to do with it
        self.unprocessed_user_input = input(
            "Please pick an option: (type 1 for option 1., etc) \n1. Save and Quit.\n2. Display all screenshots\n3. Display selected screenshots.\n4. Select screenshots by game and/or date.\n5. Select screenshot to annotate.\n6. Select and view screenshot. \n7. Delete all selected screenshots. \nYour response: "
        )
        if self.unprocessed_user_input == "1":
            # SAVE JSON HERE
            self._save_selected_files_to_json()
            self._end_main_loop()
        elif self.unprocessed_user_input == "2":
            self._display_all_screenshots()
        elif self.unprocessed_user_input == "3":
            self._display_selected_screenshots()
        elif self.unprocessed_user_input == "4":
            self._reset_requested_entries()  # clears all game_requested and date_requested values in self.main_dict["pictureIndex"] list of dictionaries, also resets user supplied self variables used to track if user supplied game, beginning and end dates
            self._select_screenshots_by_game_and_date()  # selects new screenshots for working and requested entries
        elif self.unprocessed_user_input == "5":
            self._select_and_annotate_screenshot()  # selects screenshot by ID, then allows user to submit annotation for entry
        elif self.unprocessed_user_input == "6":
            self._select_and_display_screenshot_in_default_app()  # selects screenshot by ID, then displays screenshot in default windows app
        elif self.unprocessed_user_input == "7":
            self._delete_all_selected_files()

    def format_time(
        self, unformatted_time
    ):  # cuts excess details and formats time values into yyyy-mm-dd format and returns string value of date (in yyyy-mm-dd format)
        unformatted_time = (
            unformatted_time[:7] + unformatted_time[-4:]
        )  # remove unnecessary time details

        match unformatted_time[:3]:  # convert date from name string to numeric string
            case "Jan":
                unformatted_time = "01" + unformatted_time[3:]
            case "Feb":
                unformatted_time = "02" + unformatted_time[3:]
            case "Mar":
                unformatted_time = "03" + unformatted_time[3:]
            case "Apr":
                unformatted_time = "04" + unformatted_time[3:]
            case "May":
                unformatted_time = "05" + unformatted_time[3:]
            case "Jun":
                unformatted_time = "06" + unformatted_time[3:]
            case "Jul":
                unformatted_time = "07" + unformatted_time[3:]
            case "Aug":
                unformatted_time = "08" + unformatted_time[3:]
            case "Sep":
                unformatted_time = "09" + unformatted_time[3:]
            case "Oct":
                unformatted_time = "10" + unformatted_time[3:]
            case "Nov":
                unformatted_time = "11" + unformatted_time[3:]
            case "Dec":
                unformatted_time = "12" + unformatted_time[3:]

        # format date into yyyy-m-d
        if (
            int(unformatted_time[3:5]) < 10
        ):  # add a 0 to day if day is less than 10 to fit with yyyy-mm-dd format
            unformatted_time = (
                unformatted_time[-4:]
                + "-"
                + unformatted_time[:2]
                + "-0"
                + unformatted_time[4:5]
            )
        else:  # format without adding a 0 to dd format as dd is 10 or above and doesn't need the initial 0
            unformatted_time = (
                unformatted_time[-4:]
                + "-"
                + unformatted_time[:2]
                + "-"
                + unformatted_time[3:5]
            )

        return unformatted_time  # return finalized/formatted time

    def sort_dict_by_game_and_date(
        self,
    ):  # takes self.main_dict["pictureIndex"] and sorts all values by date, then replaces self.main_dict["pictureIndex"] with all sorted entries
        sorting_dict_twwh = {}  # FOR CONTAINING DICT PRE SORT, contains screenshot_id key and entry datetime value
        sorted_dict_twwh = {}  # FOR CONTAINING DICT SORTED, contains screenshot_id key and entry datetime value
        staged_list_twwh = []  # FOR CONTAINING TWWH DICT ENTRIES SORTED BY DATE
        # sorted_list_twwh = [] # for containing screenshot_ids SORTED by DATETIME object
        sorting_dict_wow = {}
        sorted_dict_wow = {}
        staged_list_wow = []
        # sorted_list_wow = []
        sorting_dict_bg3 = {}
        sorted_dict_bg3 = {}
        staged_list_bg3 = []
        # sorted_list_bg3 = []

        all_sorted_entries = []

        for entry in self.main_dict["pictureIndex"]:  # FOR ORDERING WOW SCREENSHOTS
            entry_datetime = datetime(
                int(entry["created"][:4]),
                int(entry["created"][5:7]),
                int(entry["created"][8:]),
            )  # CREATE date time object from year, month, date of entry["created"]
            if entry["game_id"] == "wow":
                sorting_dict_wow[entry["screenshot_id"]] = (
                    entry_datetime  # FILL sorting_dict_wow DICT with key -> screenshot_id, value -> entry_datetime
                )
        sorted_dict_wow = dict(
            sorted(sorting_dict_wow.items(), key=lambda item: item[1])
        )
        for key, value in sorted_dict_wow.items():
            for entry in self.main_dict["pictureIndex"]:
                if (
                    entry["screenshot_id"] == key
                ):  # KEY IS SCREENSHOT ID IN SORTED_DICT_WOW, if key and screenshot_id for entry are the same, append into staged_list_wow.  Appends values in with ordered dates
                    staged_list_wow.append(entry)
        for entry in staged_list_wow:  # ADD SORTED WOW ENTRIES TO ALL SORTED ENTRIES LIST, all sorted entries list will be converted into self.main_dict["pictureIndex"[]
            all_sorted_entries.append(entry)

        for entry in self.main_dict["pictureIndex"]:  # FOR ORDERING TWWH SCREENSHOTS
            entry_datetime = datetime(
                int(entry["created"][:4]),
                int(entry["created"][5:7]),
                int(entry["created"][8:]),
            )  # CREATE date time object from year, month, date of entry["created"]
            if entry["game_id"] == "twwh":
                sorting_dict_twwh[entry["screenshot_id"]] = (
                    entry_datetime  # FILL sorting_dict_wow DICT with key -> screenshot_id, value -> entry_datetime
                )
        sorted_dict_twwh = dict(
            sorted(sorting_dict_twwh.items(), key=lambda item: item[1])
        )
        for key, value in sorted_dict_twwh.items():
            for entry in self.main_dict["pictureIndex"]:
                if (
                    entry["screenshot_id"] == key
                ):  # KEY IS SCREENSHOT ID IN SORTED_DICT_WOW, if key and screenshot_id for entry are the same, append into staged_list_wow.  Appends values in with ordered dates
                    staged_list_twwh.append(entry)
        for entry in staged_list_twwh:  # ADD SORTED twwh ENTRIES TO ALL SORTED ENTRIES LIST, all sorted entries list will be converted into self.main_dict["pictureIndex"[]
            # print(f"TESTING TWWH ENTRY {entry}")
            all_sorted_entries.append(entry)

        for entry in self.main_dict["pictureIndex"]:  # FOR ORDERING BG3 SCREENSHOTS
            entry_datetime = datetime(
                int(entry["created"][:4]),
                int(entry["created"][5:7]),
                int(entry["created"][8:]),
            )  # CREATE date time object from year, month, date of entry["created"]
            if entry["game_id"] == "bg3":
                sorting_dict_bg3[entry["screenshot_id"]] = (
                    entry_datetime  # FILL sorting_dict_wow DICT with key -> screenshot_id, value -> entry_datetime
                )
        sorted_dict_bg3 = dict(
            sorted(sorting_dict_bg3.items(), key=lambda item: item[1])
        )
        for key, value in sorted_dict_bg3.items():
            for entry in self.main_dict["pictureIndex"]:
                if (
                    entry["screenshot_id"] == key
                ):  # KEY IS SCREENSHOT ID IN SORTED_DICT_WOW, if key and screenshot_id for entry are the same, append into staged_list_wow.  Appends values in with ordered dates
                    staged_list_bg3.append(entry)
        for entry in staged_list_bg3:  # ADD SORTED bg3 ENTRIES TO ALL SORTED ENTRIES LIST, all sorted entries list will be converted into self.main_dict["pictureIndex"[]
            all_sorted_entries.append(entry)

        self.main_dict["pictureIndex"] = (
            all_sorted_entries  # ADD all entries SORTED back into self.main_dict["pictureIndex"]
        )

    def add_entries_to_main_dict_picture_index(
        self,
    ):  # adds all screenshots in all folders to self.main_dict["pictureIndex"]
        screenshot_id_iter = 1
        for screenshot_folder, game_id in self.screenshot_folders_and_game_ids.items():
            for path in screenshot_folder.iterdir():
                if (
                    path.is_file()
                ):  # check to make sure path is of a file and not a directory
                    if (
                        path.suffix == ".jpg"
                    ):  # check to make sure that the file is of type '.jpg'
                        temp_stats = os.stat(path)
                        unformatted_time = time.ctime(temp_stats.st_mtime)[
                            4:
                        ]  # strip out day string
                        self.main_dict["pictureIndex"].append(
                            {
                                "path": path,
                                "name": path.name,
                                "created": self.format_time(unformatted_time),
                                "game_id": game_id,
                                "screenshot_id": str(screenshot_id_iter),
                                "game_requested": False,  # to track if the game was requested
                                "date_requested": False,  # to track if the date was requested
                                "annotation": "",
                            }
                        )
                screenshot_id_iter += (
                    1  # increment screenshot_id + 1 for each entry added
                )

    def get_dict_entries_by_game_id(
        self,
    ):  # pass in main dictionary and desired game_id string
        for entry in self.main_dict["pictureIndex"]:
            if entry["game_id"] == self.user_input_game_id:
                self.working_requested_entries.append(entry)
                entry["game_requested"] = True  ### TESTING

    def get_dict_entries_if_no_game_id_specified(
        self,
    ):  # fills main dict with all screenshots if no game_id specified by user
        for entry in self.main_dict["pictureIndex"]:
            self.working_requested_entries.append(entry)
            entry["game_requested"] = (
                True  ### TESTING   # ERROR BEING CAUSED BY BLANKET ADDING ALL GAMES
            )

    def get_dict_entries_by_date_range(
        self,
    ):  # for loop to collect requested entries by date range.  Game name requested entries must be run first

        if (
            self.user_supplied_beginning_date["supplied"]
            and self.user_supplied_end_date["supplied"]
        ):  # BOTH dates supplied
            # format init dates into workable int variables
            init_date_year = int(self.user_supplied_beginning_date["date"][:4])
            init_date_month = int(self.user_supplied_beginning_date["date"][5:7])
            init_date_day = int(self.user_supplied_beginning_date["date"][8:])

            # format end dates into workable int variables
            end_date_year = int(self.user_supplied_end_date["date"][:4])
            end_date_month = int(self.user_supplied_end_date["date"][5:7])
            end_date_day = int(self.user_supplied_end_date["date"][8:])

            # format entry dates into workable int variables
            # for entry in self.working_requested_entries:
            for entry in self.main_dict["pictureIndex"]:
                entry_year = int(entry["created"][:4])
                entry_month = int(entry["created"][5:7])
                entry_day = int(entry["created"][8:])
                # print("BOTH BEGINNING AND END DATES SUPPLIED")

                # CONDITIONAL to check if entry date falls ON OR IN BETWEEN init and end dates according to yyyy-mm-dd format
                if (
                    entry_year > init_date_year and entry_year < end_date_year
                ):  # If entry year is between init year and end year, then all months and days count as in range
                    # any month is good.
                    # any day is good.
                    # self.requested_entries.append(entry)
                    entry["date_requested"] = True  ### TESTING
                    # print(entry)
                elif (
                    entry_year == init_date_year and entry_year < end_date_year
                ):  # If entry year is equal to init year but less than end year
                    if (
                        entry_month > init_date_month
                    ):  # If entry month is greater than init month then all days count as in range
                        # self.requested_entries.append(entry)
                        entry["date_requested"] = True  ### TESTING
                        # print(entry)
                    elif (
                        entry_month == init_date_month
                    ):  # If entry month is equal to init month then check if day is in range
                        if (
                            entry_day >= init_date_day
                        ):  # If entry day is greater or equal to init day then it is in range
                            # self.requested_entries.append(entry)
                            entry["date_requested"] = True  ### TESTING
                            # print(entry)
                elif (
                    entry_year > init_date_year and entry_year == end_date_year
                ):  # If entry year is equal to end year but greater than init year
                    if (
                        entry_month < end_date_month
                    ):  # If entry month is less than end month then all days count as in range
                        # self.requested_entries.append(entry)
                        entry["date_requested"] = True  ### TESTING
                        # print(entry)
                    elif (
                        entry_month == end_date_month
                    ):  # If entry month is equal to end month then check if day is in range
                        if (
                            entry_day <= end_date_day
                        ):  # If entry day is less than or equal to end day then it is in range
                            # self.requested_entries.append(entry)
                            entry["date_requested"] = True  ### TESTING
                            # print(entry)
                elif (
                    entry_year == init_date_year and entry_year == end_date_year
                ):  # if entry year is the same as init year and end year then the year is in range
                    if (
                        entry_month > init_date_month and entry_month < end_date_month
                    ):  # if entry month is greater than init month and less than end month, then all days are in range
                        # self.requested_entries.append(entry)
                        entry["date_requested"] = True  ### TESTING
                        # print(entry)
                    elif (
                        entry_month == init_date_month and entry_month < end_date_month
                    ):  # if entry month is equal to init month but less than end month
                        if (
                            entry_day >= init_date_day
                        ):  # If entry day is equal or greater than init day then it is in range
                            # self.requested_entries.append(entry)
                            entry["date_requested"] = True  ### TESTING
                            # print(entry)
                    elif (
                        entry_month > init_date_month and entry_month == end_date_month
                    ):  # If entry month is greater than init month and equal to end month
                        if (
                            entry_day <= end_date_day
                        ):  # If entry day is equal or less than end day then it is in range
                            # self.requested_entries.append(entry)
                            entry["date_requested"] = True  ### TESTING
                            # print(entry)
                    elif (
                        entry_month == init_date_month and entry_month == end_date_month
                    ):  # If entry month is the same as the init month and end month
                        if entry_day >= init_date_day and entry_day <= end_date_day:
                            # self.requested_entries.append(entry)
                            entry["date_requested"] = True  ### TESTING
                            # print(entry)

        elif self.user_supplied_beginning_date[
            "supplied"
        ]:  # ONLY beginning date supplied
            print("PROCESSING USER SUPPLIED BEGINNING DATE")
            # format init dates into workable int variables
            init_date_year = int(self.user_supplied_beginning_date["date"][:4])
            init_date_month = int(self.user_supplied_beginning_date["date"][5:7])
            init_date_day = int(self.user_supplied_beginning_date["date"][8:])

            # format entry dates into workable int variables
            # for entry in self.working_requested_entries:
            for entry in self.main_dict["pictureIndex"]:
                entry_year = int(entry["created"][:4])
                entry_month = int(entry["created"][5:7])
                entry_day = int(entry["created"][8:])
                # print("ONLY BEGINNING DATE SUPPLIED")

                # FOR ONLY BEGINNING DATE SUPPLIED
                if entry_year > init_date_year:
                    # year is good
                    # any month is good
                    # any day is good
                    # print("DATE REQUESTED")
                    entry["date_requested"] = True  ### TESTING

                elif entry_year == init_date_year:
                    # year is good
                    if entry_month > init_date_month:
                        # month is good
                        # any day is good
                        # print("DATE REQUESTED")
                        entry["date_requested"] = True  ### TESTING
                    elif entry_month == init_date_month:
                        # month is good
                        if entry_day >= init_date_day:
                            # day is good
                            # print("DATE REQUESTED")
                            entry["date_requested"] = True  ### TESTING
                        # if entry_day == init_date_day:
                        # day is good, redundant

        elif self.user_supplied_end_date["supplied"]:  # ONLY end date supplied
            # format end dates into workable int variables
            end_date_year = int(self.user_supplied_end_date["date"][:4])
            end_date_month = int(self.user_supplied_end_date["date"][5:7])
            end_date_day = int(self.user_supplied_end_date["date"][8:])

            # format entry dates into workable int variables
            for entry in self.main_dict["pictureIndex"]:
                entry_year = int(entry["created"][:4])
                entry_month = int(entry["created"][5:7])
                entry_day = int(entry["created"][8:])

                # FOR ONLY END DATE SUPPLIED
                if entry_year < end_date_year:
                    # year is good
                    # any month is good
                    # any day is good
                    entry["date_requested"] = True  ### TESTING

                elif entry_year == end_date_year:
                    # year is good
                    if entry_month < end_date_month:
                        # month is good
                        # any day is good
                        entry["date_requested"] = True  ### TESTING
                    elif entry_month == end_date_month:
                        # month is good
                        if entry_day <= end_date_day:
                            # day is good
                            entry["date_requested"] = True  ### TESTING
                        # day is good, redundant


picture_indexer = Picture_indexer()  # initialize picture indexer
picture_indexer.run_picture_indexer_main_loop()  # run picture_indexer batch mode if arguments passed on command line, or run interactive mode if no arguments passed on command line
