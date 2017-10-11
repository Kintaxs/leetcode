# Read from the file file.txt and output the tenth line to stdout.

READFILE='file.txt'

count=0

while read line
do
  if [ $count == 9 ]
  then
    echo $line
  fi
  let count=count+1
done < $READFILE
