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
SCALE=.$2 # Input variable $2 is a percentile, where 75 = 75%
TDIR=resized/$2 # Variable for our target directory (for instance, 'Poland/resized/75')

if [ $# -lt 2 ]; then
    echo "Usage: ./bulk-image-resize.sh [PATH TO FOLDER] [PERCENT]"
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
        w="${wh[0]}";h="${wh[1]}"
        # Calculate target geometry for our filename
        tw=$(echo "scale=3;$SCALE*$w" | bc)
        th=$(echo "scale=3;$SCALE*$h" | bc)
        tsize=$(echo $tw"x"$th | sed 's/\.00//g')
        # Our target image filename
        target=$(echo $img)
        echo Original size is $w"x"$h
        echo Target size is: $tsize 
        # Create a resized copy of the image to a folder in the target directory 
        echo Converting image to $target
        convert -resize $tsize $img $TDIR/$target  
    else
        echo "Not an image, leaving alone"
    fi
done
