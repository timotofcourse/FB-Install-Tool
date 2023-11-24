# This script was made to sign my tools
# i'll make a variation for other apps later

$certificate = 'F:\Certificados\timot.pfx' # This is the place i have my certificate
$passwords = Read-Host -Prompt "Enter your password: " -AsSecureString # This asks for password input to avoid showing password
$password = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($passwords))
$signfile = '.\dist\fb-install.exe' # This is the file to be signed

# Sign and timestamp

signtool sign /f $certificate /fd SHA256 /p $password $signfile
signtool timestamp -t http://timestamp.digicert.com $signfile
