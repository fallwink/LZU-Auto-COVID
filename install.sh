#!/usr/bin/env bash

# Install Dependencies
pip install -r requirements.txt

# Setup Environmental Variables
echo "---Enter your Actions Secrets, empty if it doesn't exists---"
secrets=("CARDID" "PASSWORD" "PPTOKEN" "PPTOPIC" "SERVERCHANSCKEY" "TGBOTTOKEN" "TGCHATID" "SUBSINFO" "CORPID" "CORPSECRET" "AGENTID" "CRONEXP" "DELAYS")
for secret in ${secrets[*]}
do
    read -p "-"$secret": " content
    echo "export $secret='$content'" >> envar
done

command=""
if [ -f "envar" ]; then
    command=$command"source envar && "
    command=$command"rm envar && "
fi
command=$command"python clock.py"

# Main Program Execution
eval "nohup bash -c '$command' &"
watch cat nohup.out
