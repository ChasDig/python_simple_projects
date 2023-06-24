import os

get_search_string = input("Input search text: ")
get_path_dir = input("Input path directory: ")


def sear_string_in_file(search_string, path_file: str):
    try:
        with open(path_file, "r") as file:
            if search_string in file.read():
                return True
            return False
    except Exception as ex:
        print(f"[!!]Error in func 'sear_string_in_file': {ex}")


def get_count_file(search_string: str, path_dir: str):
    count_files = 0
    try:
        abs_path = os.path.abspath(path=path_dir)
        all_elements = os.listdir(path=abs_path)
        for element in all_elements:
            path_element = abs_path + f"/{str(element)}"
            if os.path.isfile(path=path_element):
                if sear_string_in_file(search_string, path_element):
                    count_files += 1
            if os.path.isdir(path_element):
                count_files += get_count_file(search_string, path_dir=path_element)
    except FileNotFoundError as _:
        print(f"[!!]Error in func 'get_file': File not found on path '{path_dir}'")
    except Exception as ex:
        print(f"[!!]Error in func 'get_file': {ex}")
    return count_files


if __name__ == "__main__":
    res = get_count_file(search_string=get_search_string, path_dir=get_path_dir)
    print(f"Count files with string '{get_search_string}' in directory '{get_path_dir}' is {res}.")
