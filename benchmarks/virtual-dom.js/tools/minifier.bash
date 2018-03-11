#!/usr/bin/env bash

google-closure-compiler-js \
  --externs=<(echo 'let module') \
  --compilationLevel=ADVANCED \
  --assumeFunctionWrapper \
  --languageOut=ES6 \
  | grep --invert-match ES3 \
  | tr --delete '\n' \
  | sed "s/'use strict';//" \
  | sed --regexp-extended 's/Object.assign\(\{\},(\w+),(\w+)\)/{...\1,...\2}/'
