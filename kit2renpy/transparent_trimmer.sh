#!/bin/bash

# Resize all images in the given folder to a percentile. 
# Requires ImageMagick via your GNU/Linux distribution or OS at https://www.imagemagick.org/
# 
# Save as bulk-image-resize.sh, 'chmod +x bulk-image-resize.sh' and run:
#
#   ./bulk-image-resize.sh [PATH TO FOLDER] [PERCENT]
#
# You're welcome,
# Julian Oliver, 2018 
# https://julianoliver.com

DIR=$1 #fullpath
TDIR=trimmed # Variable for our target directory (for instance, 'Poland/resized/75')

if [ $# -lt 1 ]; then
    echo "Usage: ./bulk-image-resize.sh [PATH TO FOLDER]"
    exit 0
fi

cd $DIR

# Check for target directory, create if it doesn't already exist 
if [ ! -d $TDIR ]; then
    mkdir -p $TDIR
else
    echo "Directory $TDIR already exists"
fi

for img in *; do  
    # Check we're working with images 
    ft=$(file $img |  awk '{split($0,a,":"); split($0,b," "); print $3}')
    if [[ $ft == "image" ]]; then
        echo Found image $img
        # Get width and height of original image
        wh=($(identify $img | awk '{ gsub(/x/," "); print $3" "$4 }'))
        
        convert $img -trim $img  
    else
        echo "Not an image, leaving alone: " $img
    fi
done
