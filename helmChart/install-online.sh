#!/usr/bin/env bash

kubectl create ns lzu-auto-covid-health-report
# Add Repo
helm repo add LZU-Auto-COVID-Health-Report http://hollowman.ml/LZU-Auto-COVID-Health-Report
helm repo update
# Install
echo "---Enter your Actions Secrets, empty if it doesn't exists---"
secrets=("cardID" "password" "serverChanSCKey" "ppToken" "ppTopic" "tgBotToken" "tgChatID" "corpID" "corpSecret" "agentID" "subsInfo")
command="helm install lzu-auto-covid-health-report LZU-Auto-COVID-Health-Report/lzu-auto-covid-health-report --namespace lzu-auto-covid-health-report"
for secret in ${secrets[*]}
do
    read -p "-"$secret": " content
    command=$command" --set "$secret"="$content
done
$command
