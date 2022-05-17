#!/bin/bash
test() {
    echo Testing $1
    diff <(python3 wallet.py <<< $1 | tee wallet.log) <(./test-bitcoin-tool.sh $1 | tee bitcoin-tool.log)
}

while read -r key
do
    test $key
done < test.keys

RANDOM=777
SEQ=10000

seq $SEQ | xargs -I{} -n 1 -P 1 /bin/bash -c "echo {} | sha256sum" | cut -d" " -f1 | while read -r key
do
    test $key
done
