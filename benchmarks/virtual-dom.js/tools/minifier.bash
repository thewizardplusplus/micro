#!/usr/bin/env bash

google-closure-compiler-js \
  --externs=<(echo 'let module') \
  --compilationLevel=ADVANCED \
  --assumeFunctionWrapper \
  --languageOut=ES6 \
  | grep --invert-match ES3
