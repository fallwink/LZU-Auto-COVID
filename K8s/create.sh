#!/usr/bin/env bash

# Setup Secrets
echo "---Enter your Actions Secrets, empty if it doesn't exists---"
secrets=("cardid" "password" "serverchansckey" "pptoken" "pptopic" "tgbottoken" "tgchatid" "corpid" "corpsecret" "agentid" "subsinfo")
command="kubectl create secret generic lzu-auto-covid-health-report-secrets"
for secret in ${secrets[*]}
do
    read -p "-"$secret": " content
    command=$command" --from-literal="$secret"="$content
done
$command

# Create cronJob
kubectl create -f LZU-Auto-COVID-Health-Report.yml

# Check Details
kubectl get secret/lzu-auto-covid-health-report-secrets configmap/lzu-auto-covid-health-report-configmap cronjob/lzu-auto-covid-health-report
