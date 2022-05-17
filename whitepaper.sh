#!/bin/sh
echo "With txindex:"
bitcoin-cli getrawtransaction 54e48e5f5c656b26c3bca14a8c95aa583d07ebe84dde3b7dd4a78f4e4186e713 | sed 's/0100000000000000/\n/g' | tail -n +2 | cut -c7-136,139-268,271-400 | tr -d '\n' | cut -c17-368600 | xxd -p -r > bitcoin.pdf

echo "Without txindex:"
bitcoin-cli getblock 00000000000000ecbbff6bafb7efa2f7df05b227d5c73dca8f2635af32a2e949 2 | jq '.tx | .[] | select(.txid=="54e48e5f5c656b26c3bca14a8c95aa583d07ebe84dde3b7dd4a78f4e4186e713").hex' -r | sed 's/0100000000000000/\n/g' | tail -n +2 | cut -c7-136,139-268,271-400 | tr -d '\n' | cut -c17-368600 | xxd -p -r > bitcoin.pdf

echo "Without txindex, no json:"
bitcoin-cli getblock 00000000000000ecbbff6bafb7efa2f7df05b227d5c73dca8f2635af32a2e949 0 | tail -c+92167 | for ((o=0;o<946;++o)) ; do read -rN420 x ; echo -n ${x::130}${x:132:130}${x:264:130} ; done | xxd -r -p | tail -c+9 | head -c184292 > bitcoin.pdf

echo "From web (blockchain.info):"
curl https://blockchain.info/block/00000000000000ecbbff6bafb7efa2f7df05b227d5c73dca8f2635af32a2e949?format=hex | tail -c+92167 | for ((o=0;o<946;++o)) ; do read -rN420 x ; echo -n ${x::130}${x:132:130}${x:264:130} ; done | xxd -r -p | tail -c+9 | head -c184292 > bitcoin.pdf
