#!/bin/bash

filename="$1"
old_str="$2"
new_str="$3"
bak_file="${filename}.bak"
tmp_file="${filename}.tmp"

if [[ -f $filename ]]; then
  if [[ ! -f "$bak_file" ]]; then
    echo "backup resource file to"
    cp -r "$filename" "$bak_file"
  fi
  buffer=$(cat $filename | awk -v RS= '{gsub(/($old_str)/, "$new_str"); print}')
  if [[ "$?" != 0 ]]; then
    echo "failed to replace string, filename: $filename"
  else
    echo "$buffer" > "$tmp_file"
    if [[ "$?" == 0 ]]; then
      mv "$tmp_file" $filename || true
    fi
    echo "success"
  fi
else
  echo "no such file or directory, $filename"
fi
