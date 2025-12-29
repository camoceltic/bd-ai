import os

def get_files_info(working_directory, directory = "."):
    absolute_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(absolute_path, directory))
    valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    target_dir_contents = []

    for i in os.listdir(target_dir):
        target_dir_contents.append(f"  - {i}: file_size={os.stat(target_dir + '/' + i).st_size}bytes, is_dir={os.path.isdir(target_dir + '/' + i)}")
    
    return target_dir_contents

