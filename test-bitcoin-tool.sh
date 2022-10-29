#!/bin/sh
TEST="tests/$1.test"
if [ -f "$TEST" ]; then
    cat "$TEST"
else

WIFXY=$(bitcoin-tool --input-type private-key --input-format hex --output-type private-key-wif --output-format base58check --network bitcoin --public-key-compression uncompressed --input $1)
WIFX=$(bitcoin-tool --input-type private-key --input-format hex --output-type private-key-wif --output-format base58check --network bitcoin --public-key-compression compressed --input $1)
ADDRXY=$(bitcoin-tool --input-type private-key --input-format hex --output-type address --output-format base58check --network bitcoin --public-key-compression uncompressed --input $1)
ADDRX=$(bitcoin-tool --input-type private-key --input-format hex --output-type address --output-format base58check --network bitcoin --public-key-compression compressed --input $1)
ADDRBECH32=$(bitcoin-tool --input-type private-key --input-format hex --output-type address --output-format bech32 --network bitcoin --public-key-compression compressed --input $1)
(cat << EOF
                   Privkey (HEX) : $1
                Privkey (WIF XY) : $WIFXY
                 Privkey (WIF X) : $WIFX
                    Address (XY) : $ADDRXY
                     Address (X) : $ADDRX
                Address (Bech32) : $ADDRBECH32
EOF
) | tee "$TEST"

fi
