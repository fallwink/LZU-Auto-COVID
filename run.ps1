# Install Dependencies
pip install -r requirements.txt

# Setup Environmental Variables
Write-Host "---Enter your Actions Secrets, empty if it doesn't exists---"
$secrets = "CARDID", "PASSWORD", "PPTOKEN", "PPTOPIC", "SERVERCHANSCKEY", "TGBOTTOKEN", "TGCHATID", "SUBSINFO", "CORPID", "CORPSECRET", "AGENTID", "CRONEXP", "DELAYS"
ForEach ($secret in $secrets) {
    $content = Read-Host ('-' + $secret)
    if (!$content) {
        $content = 'NONE'
    }
    $cmd = '$env:' + "$secret='$content'"
    Invoke-Expression $cmd
}

& "python" "clock.py"
