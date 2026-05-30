import json
import os
import time
from pathlib import Path

from PIL import Image

picture_store = {"pictureIndex": []}

initial_input = ""

if initial_input == "add":
    pass
elif initial_input == "annotate":
    pass
elif initial_input == "search":
    pass

print("Thank you for using the picture index program")
# initial_input = input('Please input your option: "add", "annotate", "search": ')
# print(f"Your input was : {initial_input}")


# create a path object for directory
wow_folder = Path("C:/Users/Zen/Desktop/example_screenshots/WOW")
twwh_folder = Path("C:/Users/Zen/Desktop/example_screenshots/TWWH")
bg3_folder = Path("C:/Users/Zen/Desktop/example_screenshots/BG3")

wow_screenshots_folder = Path(
    "C:/Program Files (x86)/World of Warcraft/_retail_/Screenshots"
)
wow_game_id = "wow"
twwh_screenshots_folder = Path(
    "C:/Program Files (x86)/Steam/userdata/109185688/760/remote/1142710/screenshots"
)
twwh_game_id = "twwh"
bg3_screenshots_folder = Path(
    "C:/Program Files (x86)/Steam/userdata/109185688/760/remote/1086940/screenshots"
)
bg3_game_id = "bg3"

# print(bg3_folder)

# wow_files = [f.name for f in wow_folder.iterdir() if f.is_file()]
# bg3_files = [f.name for f in bg3_folder.iterdir() if f.is_file()]
# print(str(bg3_folder) + bg3_files[0])
# print(wow_files)

# bg3_path_files = [f.resolve() for f in bg3_folder.iterdir() if f.is_file()]
# print(bg3_path_files)
# print(wow_path_files)
#

wow_path_files_test = []
bg3_path_files_test = []
twwh_path_files_test = []

wow_info_dict = {}
bg3_info_dict = {}
twwh_info_dict = {}

main_dict = {"pictureIndex": []}

# main_dict["pictureIndex"].append({"test": "test_value"})

# print()
# print(main_dict)
# print()


def format_time(unformatted_time):
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


# for path in bg3_screenshots_folder.iterdir():   # non testing bg3 pictures folder
#     # bg3_path_files_test.append(str(path)) #for testing and printing
#     # print(path)
#     # print(type(path))
#     if path.is_file():  # check to make sure path is of a file and not a directory
#         if path.suffix == ".jpg":  # check to make sure that the file is of type '.jpg'
#             temp_stats = os.stat(path)
#             unformatted_time = time.ctime(temp_stats.st_mtime)[
#                 4:
#             ]  # strip out day string
#             main_dict["pictureIndex"].append(
#                 {
#                     "path": path,
#                     "name": path.name,
#                     "created": format_time(unformatted_time),
#                     "game_id": "bg3",
#                 }
#             )
def add_entries_to_main_dict_picture_index(screenshots_folder, game_id):
    for path in screenshots_folder.iterdir():  # FOR TESTING WITH SMALLER AMOUNT OF ENTRIES    #### TESTING ONLY #### TESTING ONLY ####
        # bg3_path_files_test.append(str(path)) #for testing and printing
        # print(path)
        # print(type(path))
        if path.is_file():  # check to make sure path is of a file and not a directory
            if (
                path.suffix == ".jpg"
            ):  # check to make sure that the file is of type '.jpg'
                temp_stats = os.stat(path)
                unformatted_time = time.ctime(temp_stats.st_mtime)[
                    4:
                ]  # strip out day string
                main_dict["pictureIndex"].append(
                    {
                        "path": path,
                        "name": path.name,
                        "created": format_time(unformatted_time),
                        "game_id": game_id,
                    }
                )


# for path in bg3_screenshots_folder.iterdir():  # FOR TESTING WITH SMALLER AMOUNT OF ENTRIES    #### TESTING ONLY #### TESTING ONLY ####
#     # bg3_path_files_test.append(str(path)) #for testing and printing
#     # print(path)
#     # print(type(path))
#     if path.is_file():  # check to make sure path is of a file and not a directory
#         if path.suffix == ".jpg":  # check to make sure that the file is of type '.jpg'
#             temp_stats = os.stat(path)
#             unformatted_time = time.ctime(temp_stats.st_mtime)[
#                 4:
#             ]  # strip out day string
#             main_dict["pictureIndex"].append(
#                 {
#                     "path": path,
#                     "name": path.name,
#                     "created": format_time(unformatted_time),
#                     "game_id": "bg3",
#                 }
#             )
#             # print("APPENDING")


# for path in wow_screenshots_folder.iterdir():
#     # bg3_path_files_test.append(str(path)) #for testing and printing
#     # print(path)
#     # print(type(path))
#     if path.is_file():  # check to make sure path is of a file and not a directory
#         if path.suffix == ".jpg":  # check to make sure that the file is of type '.jpg'
#             temp_stats = os.stat(path)
#             unformatted_time = time.ctime(temp_stats.st_mtime)[
#                 4:
#             ]  # strip out day string
#             main_dict["pictureIndex"].append(
#                 {
#                     "path": path,
#                     "name": path.name,
#                     "created": format_time(unformatted_time),
#                     "game_id": "wow",
#                 }
#             )

# for path in twwh_screenshots_folder.iterdir():
#     # bg3_path_files_test.append(str(path)) #for testing and printing
#     # print(path)
#     # print(type(path))
#     if path.is_file():  # check to make sure path is of a file and not a directory
#         if path.suffix == ".jpg":  # check to make sure that the file is of type '.jpg'
#             temp_stats = os.stat(path)
#             unformatted_time = time.ctime(temp_stats.st_mtime)[
#                 4:
#             ]  # strip out day string
#             main_dict["pictureIndex"].append(
#                 {
#                     "path": path,
#                     "name": path.name,
#                     "created": format_time(unformatted_time),
#                     "game_id": "twwh",
#                 }
#             )

# for path in wow_folder.iterdir():
#     # bg3_path_files_test.append(str(path)) #for testing and printing
#     # print(path)
#     # print(type(path))

#     temp_stats = os.stat(path)
#     unformatted_time = time.ctime(temp_stats.st_mtime)[4:]  # strip out day string

#     main_dict["pictureIndex"].append(
#         {"path": path, "created": format_time(unformatted_time)}
#     )

# for path in twwh_folder.iterdir():
#     # bg3_path_files_test.append(str(path)) #for testing and printing
#     # print(path)
#     # print(type(path))

#     temp_stats = os.stat(path)
#     unformatted_time = time.ctime(temp_stats.st_mtime)[4:]  # strip out day string

#     main_dict["pictureIndex"].append(
#         {"path": path, "created": format_time(unformatted_time)}
#     )
working_requested_entries = []  # list for containing working set of requested entries from user
requested_entries = []  # finalized list containing requested user entries by game name and date

# date_range format: yyyy-mm-dd -> yyyy-mm-dd
date_range = ("2023-08-08", "2023-11-13")  # TEST user supplied date range


# print(main_dict)
# print(main_dict["pictureIndex"][0]["path"].name)

# for entry in main_dict[
#     "pictureIndex"
# ]:  # for loop to collect requested entries by game name
#     if entry["game_id"] == "bg3":
#         working_requested_entries.append(entry)


def get_dict_entries_by_game_id(
    main_dict, game_id
) -> list:  # pass in main dictionary and desired game_id string
    working_requested_entries = []
    for entry in main_dict["pictureIndex"]:
        if entry["game_id"] == game_id:
            working_requested_entries.append(entry)

    return working_requested_entries


def get_dict_entries_by_date_range(
    date_range, working_requested_entries
):  # for loop to collect requested entries by date range.  Game name requested entries must be run first

    # print(date_range)

    # format init dates into workable int variables
    init_date_year = int(date_range[0][:4])
    init_date_month = int(date_range[0][5:7])
    init_date_day = int(date_range[0][8:])

    # print(init_date_year)
    # print(init_date_month)
    # print(init_date_day)

    # format end dates into workable int variables
    end_date_year = int(date_range[1][:4])
    end_date_month = int(date_range[1][5:7])
    end_date_day = int(date_range[1][8:])

    # print(end_date_year)
    # print(end_date_month)
    # print(end_date_day)

    # format entry dates into workable int variables
    for entry in working_requested_entries:
        entry_year = int(entry["created"][:4])
        entry_month = int(entry["created"][5:7])
        entry_day = int(entry["created"][8:])
        # print(entry)
        # print(entry_year)
        # print(init_date_year)
        # print(end_date_year)

        # CONDITIONAL to check if entry date falls ON OR IN BETWEEN init and end dates according to yyyy-mm-dd format
        if (
            entry_year > init_date_year and entry_year < end_date_year
        ):  # If entry year is between init year and end year, then all months and days count as in range
            # any month is good.
            # any day is good.
            requested_entries.append(entry)
        elif (
            entry_year == init_date_year and entry_year < end_date_year
        ):  # If entry year is equal to init year but less than end year
            if (
                entry_month > init_date_month
            ):  # If entry month is greater than init month then all days count as in range
                requested_entries.append(entry)
            elif (
                entry_month == init_date_month
            ):  # If entry month is equal to init month then check if day is in range
                if (
                    entry_day >= init_date_day
                ):  # If entry day is greater or equal to init day then it is in range
                    requested_entries.append(entry)
        elif (
            entry_year > init_date_year and entry_year == end_date_year
        ):  # If entry year is equal to end year but greater than init year
            if (
                entry_month < end_date_month
            ):  # If entry month is less than end month then all days count as in range
                requested_entries.append(entry)
            elif (
                entry_month == end_date_month
            ):  # If entry month is equal to end month then check if day is in range
                if (
                    entry_day <= end_date_day
                ):  # If entry day is less than or equal to end day then it is in range
                    requested_entries.append(entry)
        elif (
            entry_year == init_date_year and entry_year == end_date_year
        ):  # if entry year is the same as init year and end year then the year is in range
            if (
                entry_month > init_date_month and entry_month < end_date_month
            ):  # if entry month is greater than init month and less than end month, then all days are in range
                requested_entries.append(entry)
            elif (
                entry_month == init_date_month and entry_month < end_date_month
            ):  # if entry month is equal to init month but less than end month
                if (
                    entry_day >= init_date_day
                ):  # If entry day is equal or greater than init day then it is in range
                    requested_entries.append(entry)
            elif (
                entry_month > init_date_month and entry_month == end_date_month
            ):  # If entry month is greater than init month and equal to end month
                if (
                    entry_day <= end_date_day
                ):  # If entry day is equal or less than end day then it is in range
                    requested_entries.append(entry)
            elif (
                entry_month == init_date_month and entry_month == end_date_month
            ):  # If entry month is the same as the init month and end month
                if (
                    entry_day > init_date_day and entry_day < end_date_day
                ):  # If entry is greater than init day and less than end day then it is in range
                    requested_entries.append(entry)
                if (
                    entry_day == init_date_day and entry_day < end_date_day
                ):  # If entry is equal to init day and less than end day then it is in range
                    requested_entries.append(entry)
                elif (
                    entry_day > init_date_day and entry_day == end_date_day
                ):  # If entry is greater than init day and equal to end day then it is in range
                    requested_entries.append(entry)
                elif (
                    entry_day == init_date_day and entry_day == end_date_day
                ):  # If entry day is equal to init day and equal to end day then it is in range
                    requested_entries.append(entry)

    # if entry_year >= init_date_year and entry_year <= end_date_year:
    #   working_requested_entries.append(entry)

    # if main_dict["pictureIndex"][entry]["game_id"] == "bg3":
    #    print(entry)


add_entries_to_main_dict_picture_index(wow_screenshots_folder, wow_game_id)
add_entries_to_main_dict_picture_index(twwh_screenshots_folder, twwh_game_id)
add_entries_to_main_dict_picture_index(bg3_screenshots_folder, bg3_game_id)

working_requested_entries = get_dict_entries_by_game_id(main_dict, "wow")
get_dict_entries_by_date_range(date_range, working_requested_entries)


for entry in working_requested_entries:
    print(entry)
print("PRINTING REQUESTED ENTRIES")
for entry in requested_entries:
    print(entry)

# for key, value in main_dict["pictureIndex"]:
# print(key)
# print()
# print(value)
# bg3_info_dict[str(path)] = format_time(unformatted_time)

# formatted_time = unformatted_time[:7] + unformatted_time[-4:]

# print(formatted_time[:3])

# match formatted_time[:3]:
#     case "Jan":
#         formatted_time = "01" + formatted_time[3:]
#     case "Feb":
#         formatted_time = "02" + formatted_time[3:]
#     case "Mar":
#         formatted_time = "03" + formatted_time[3:]
#     case "Apr":
#         formatted_time = "04" + formatted_time[3:]
#     case "May":
#         formatted_time = "05" + formatted_time[3:]
#     case "Jun":
#         formatted_time = "06" + formatted_time[3:]
#     case "Jul":
#         formatted_time = "07" + formatted_time[3:]
#     case "Aug":
#         formatted_time = "08" + formatted_time[3:]
#     case "Sep":
#         formatted_time = "09" + formatted_time[3:]
#     case "Oct":
#         formatted_time = "10" + formatted_time[3:]
#     case "Nov":
#         formatted_time = "11" + formatted_time[3:]
#     case "Dec":
#         formatted_time = "12" + formatted_time[3:]

# formatted_time = (
#     formatted_time[-4:] + "-" + formatted_time[:2] + "-" + formatted_time[3:6]
# )


# for path in wow_folder.iterdir():
#    wow_path_files_test.append(str(path))
# for path in twwh_folder.iterdir():
#    twwh_path_files_test.append(str(path))

# for path in wow_path_files_test:
#    temp_stats = os.stat(path)
#    wow_info_dict[path] = time.ctime(temp_stats.st_mtime)

# for path in bg3_path_files_test:
#     temp_stats = os.stat(path)
#     bg3_info_dict[path] = time.ctime(temp_stats.st_mtime)

# for path in twwh_path_files_test:
#    temp_stats = os.stat(path)
#    twwh_info_dict[path] = time.ctime(temp_stats.st_mtime)


# for path in wow_path_files:
#    print(path)

# for path in wow_path_files:
#     print(path)
#     wow_picture_file_paths.append(path)
#     temp_stats = os.stat(path)
#     wow_info_dict[path] = time.ctime(temp_stats.st_mtime)
#

# for key, value in bg3_info_dict.items():
#    print(f"{key} : {value}")
# value = value[:4]

# print(wow_info_dict)
# print(bg3_info_dict)
# print(twwh_info_dict)
# print(wow_info_dict)

# for path in wow_picture_file_paths:
#    print(path)

# for key, value in main_dict.items():
#    print(key)
#    print(value)

# print(main_dict["pictureIndex"])

# for dict in main_dict["pictureIndex"]:
#    print(dict)
