#!/usr/bin/env bash

# Setup Environmental Variables
env -0 | while IFS='=' read -r -d '' n v; do
    if [ ${n#INPUT_} != $n ]
    then
        echo "export ${n#INPUT_}='$v'" >> /envar
    fi
done
if [ -f "/envar" ]; then
    source /envar
fi

# Main Program Execution
if [ ! -z $DELAYS ]
then
    if [ ! -d "/cache" ] || [ -f "/cache/runned" ]
    then
        echo "---Wait for $DELAYS---"
        sleep $DELAYS
    elif [ -d "/cache" ]
    then
        touch "/cache/runned"
    fi
fi
echo "---Auto COVID Health Report---"
if python /LZU-Auto-COVID-Health-Report.py >> information.txt && cat information.txt;
then
    echo "---Notify Success Using ServerChan or PushPlus---"
    python /Notify-Using-SeverChan-Or-PushPlus.py success
else
    echo "---Error logging and Notifying Using ServerChan or PushPlus---"
    python /Notify-Using-SeverChan-Or-PushPlus.py failure && cat information.txt
    exit 1
fi
