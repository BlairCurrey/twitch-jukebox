'''
This script moves all the song files from subfolders and puts them in 
main song folder.

Needs work. Configured to run within the song directory (see below)

root
|_songs
    |_script
    |   |_this_script.py
    |_song_dir1
    |_song_dir2
    etc.

Should execute from outside song directoty. 
Also, when I ran it I saw a weird behavior where it did not copy to
the expected location.
'''

from pathlib import Path

target_dir = (Path(__file__).resolve().parent.parent)

# get list of directories in songs
sub_dirs = [sub_dirs for sub_dirs in target_dir.iterdir()]
# remove the directory this script is located in from list
sub_dirs.remove(Path(__file__).resolve().parent)

# move each file in each sub directory to target directory
for sub_dir in sub_dirs:
    for each_file in sub_dir.iterdir():
        # print(target_dir.joinpath(each_file.name))
        # target directory is not quite right
        each_file.rename(target_dir.joinpath(each_file.name))