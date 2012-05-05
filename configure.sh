#!/bin/bash

# Enter boost directory here (or you will be prompted to type it)
BOOSTPATH=''

if [ -z $BOOSTPATH ]
then
    echo -n "Enter full path to boost directory (need not be compiled) [ENTER]: "
    read BOOSTPATH
fi

if [ -n "$BOOSTPATH" ]
then
	sed -i -e "s:INSERT_PATH_TO_BOOST_SRC:$BOOSTPATH:g" tokenizer/src/Make.common
fi

cat > Makefile <<_EOF_
build:
	make -C tokenizer/src
	mv tokenizer/src/vera++ tokenizer/

clean:
	make -C tokenizer/src clean
	rm -f tokenizer/vera++
_EOF_

