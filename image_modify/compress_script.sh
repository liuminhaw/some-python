#!/bin/bash

# Use image_modify.py program to compress images in given directory

USAGE='USAGE: compress_script.sh SOURCE DESTINATION [QUALITY]'

# Check input argument numbers
if [[ ${#} -lt 2 ]]; then
  echo "${USAGE}"
  exit 1
fi

# Assign source directory
SOURCE=${1}
DESTINATION=${2}
QUALITY=${3}

# Run image_modify.py on each file in the directory
for FILE in $(ls ${SOURCE}); do
  FULL_SOURCE_PATH=$(cd ${SOURCE} && pwd -P)/${FILE}
  FULL_DEST_PATH=$(cd ${DESTINATION} && pwd -P)
  ./image_modify.py compress ${FULL_SOURCE_PATH} ${FULL_DEST_PATH} ${QUALITY}

  # Check return value of image_modify.py program
  if [[ ${?} != 0 ]]; then
    echo "Failed to compress ${FULL_SOURCE_PATH}"
  fi
done

exit 0
