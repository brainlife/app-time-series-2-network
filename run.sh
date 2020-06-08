#!/bin/bash

set -e
set -x

# if py_bin not exported to script, use "python3"
if [[ -z ${py_bin} ]] ; then
	py_bin=python3
fi

EXEDIR=$(dirname "$(readlink -f "$0")")/

###############################################################################

# where to output stuff
inOUTBASE=${PWD}/

# read inputs from jq

# required
inTS=`jq -r '.timeseries' config.json`
inDiscard=`jq -r '.discard' config.json`
inSimType=`jq -r '.similaritymeas' config.json`

################################################################################

# check the main stuff we need
if [[ ${inTS} = "null" ]] ; then
	echo "ERROR: need a time series" >&2;
	exit 1
fi

if [[ ${inDiscard} = "null" ]] ; then
	inDiscard=0
fi

###############################################################################
# run it

mkdir -p ${inOUTBASE}/output_network/

cmd="${py_bin} ${EXEDIR}/src/makenetwork.py \
		-out ${inOUTBASE}/output_network/out \
		${inTS} \
		-discardframes ${inDiscard} \
	"
if [[ ${inSimType} != "null" ]] ; then
  cmd="${cmd} -type ${inSimType}"
fi
echo $cmd
eval $cmd

outNet=$(ls ${inOUTBASE}/output_network/out_*_connMatdf.csv)
if [[ ! -e ${outNet} ]] ; then
	echo "connMatdf not made, problem" >&2; 
	exit 1
else
	# rename it
	mv $outNet ${inOUTBASE}/output_network/out_connMatdf.csv
fi

###############################################################################
# generate cm

cmd="${py_bin} ${EXEDIR}/src/generate_cm_datatype.py"
echo $cmd
eval $cmd

# end run.sh
