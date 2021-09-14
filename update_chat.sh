#!/usr/bin/env bash

cd helmChart
helm package ./lzu-auto-covid-health-report
cd ..
helm repo index . --url http://hollowman.ml/LZU-Auto-COVID-Health-Report