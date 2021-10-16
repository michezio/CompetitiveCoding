#! /bin/bash

source ./rubik/bin/activate
cd archives

for i in {127..0}
do
    pass=$(python ../solve.py "password${i}.txt")
    7z x "archive${i}.zip" -aoa -p$pass &> /dev/null
    echo "PASSWORD $i: $pass"
done

cat flag.txt; echo "FLAG: "

cd ..