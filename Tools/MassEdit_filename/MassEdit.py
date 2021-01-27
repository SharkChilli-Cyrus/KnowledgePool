import sys
import os
import re

def mass_edit_filename(folder_path):
    folder_name = os.path.basename(folder_path)

    filename_list = []
    filename_list = os.listdir(folder_path)
    file_count = len(filename_list)

    unchanged_files = []
    count = 0
    for filename in filename_list:
        if not filename.startswith("."):
            file_type = filename.split(".")[-1]
            try:
                numbers = re.findall("\d+", filename)
                number = ""
                for i in numbers:
                    number = number + "-" + i
                number = number.strip("-")

                new_filename = "{0}{1}.{2}".format(
                    folder_name,
                    number,
                    file_type
                )

                os.rename(
                    os.path.join(folder_path, filename),
                    os.path.join(folder_path, new_filename)
                )

                count += 1
            except:
                unchanged_files.append(filename)
        else:
            unchanged_files.append(filename)
            
    print("*\n===== Mass Edit - Filename")
    print("* Folder Name: {0}".format(folder_name))
    print("* In Total {0} File".format(file_count))
    print("* Changed {0} Filenames".format(count))
    print("* Unchanged Files: {0}".format(len(unchanged_files)))
    for unchanged_file in unchanged_files:
        print("\t- {0}".format(unchanged_file))


if __name__ == "__main__":
    folder_path = input("Please Enter Your Folder Path:")

    mass_edit_filename(folder_path)
