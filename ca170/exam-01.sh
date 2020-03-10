if test "$2" = ""
then
 echo "Error. Not enough arguments."
 exit
fi

# Read in the arguments:

OLDSTRING=$1
NEWSTRING=$2

cd $HOME/shakespeare/macbeth

for file in *html
do
 cat $file | sed -e "s|$OLDSTRING|$NEWSTRING|g" > tmpfile
 mv tmpfile $file
done