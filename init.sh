#!/bin/zsh
##
## Initialize college pc's for use with git
##

git config user.name "cawnj"
git config user.email "conorjoyce2000@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
git pull

echo
echo ~~~~~~~
echo "Done!"
echo ~~~~~~~
echo