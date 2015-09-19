#!/bin/bash

# This script, when run, creates a New Folder and moves all the files and folders in the current folder to it.
# Useful mostly to clean desktop or archive things.

echo "Specify the directory(either relative/absolute path) where you want this script to run.\n Note: Do not use ~.Do not end with /"
read dir_path

echo "Enter the New Folder name."
read folder_name

final_path="$dir_path/$folder_name"

final_path2="$dir_path/*"

mkdir $final_path

mv $final_path2 $final_path
