#!/bin/bash

# This script, when run, creates a New Folder and moves all the files and folders in the current folder to it.
# Useful mostly to clean desktop or archive things.

echo "Specify the directory(either relative/absolute path) where you want this script to run.\n Note: Do not use ~.Do not end with /"
read dir_path

echo "Enter the New Folder name."
read folder_name

final_path="$dir_path/$folder_name"

temp_path="$dir_path/../$folder_name"

mkdir $temp_path

mv ${dir_path} $temp_path

mkdir -p $dir_path

mv $temp_path $dir_path 