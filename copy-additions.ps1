
$icon = '.\icon.ico'
$data = '.\data.yml'
$dest = '.\dist'
$icondest = $dest + $icon
$datadest = $dest + $data


Copy-Item -Path $icon -Destination $icondest
Copy-Item -Path $data -Destination $datadest
Copy-Item -Path ".\apps.yaml" -Destination ".\dist\apps.yaml"