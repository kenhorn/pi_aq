#! /bin/sh

pid=$(ps -ef | grep 03_data_logger.py | grep -v grep | awk '{print $2}')

if [ $1 = "--stop" ]; then
  echo "killing $pid"
  kill $pid
  exit
fi

if [ $1 = "--restart" ]; then
  shift
  echo "killing $pid"
  kill $pid
  unset pid
fi

period=$1
shift
suffix=$1
shift

if [ -z $pid ]; then
  # not running
  stub=$(date +%Y%m%d-%H%M)-$suffix
  nohup python3 03_data_logger.py $period $stub.txt > $stub.log 2>&1 &
  echo started $$
fi

