#!/bin/bash

git config user.name "cawnj"
git config user.email "conorjoyce2000@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
git pull

echo
echo "Done!"