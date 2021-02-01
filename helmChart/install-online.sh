#!/usr/bin/env bash

# Add Repo
helm repo add LZU-Auto-COVID-Health-Report http://hollowman.ml/LZU-Auto-COVID-Health-Report

# Install
echo "---Enter your Actions Secrets, empty if it doesn't exists---"
secrets=("cardID" "password" "serverChanSCKey" "openID" "ppToken" "ppTopic")
command="helm install LZU-Auto-COVID-Health-Report/lzu-auto-covid-health-report lzu-auto-covid-health-report"
for secret in ${secrets[*]}
do
    read -p "-"$secret": " content
    command=$command" --set "$secret"='"$content"'"
done
$command
