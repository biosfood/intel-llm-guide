#!/bin/bash

# Arguments: <model_id>
# the model_id is of the form "<user>/<model_name>"

model_id=$1
user=${model_id%%/*}
model_name=${model_id##*/}

printf "Cloning model %s / %s\n" $user $model_name

mkdir -p /opt/models/$user
pushd /opt/models/$user
 git lfs install
 # using the deprecated git lfs clone for now because it gives
 # some info on the progress of the clone
 git lfs clone git@hf.co:$model_id -v --progress
popd
