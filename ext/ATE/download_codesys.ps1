# Define the source and destination paths
$sourceFilePath = "T:\RDProjects\Ohjelmistot\CoDeSys\CODESYS 64 3.5.18.0.exe"  # Replace with the actual network file path
$destinationFolderPath = "$HOME\Downloads\CODESYS 64 3.5.18.0.exe"  # Replace with the local folder where you want to save the file

# Check if the source file exists
if (Test-Path $sourceFilePath -PathType Leaf) {
    # Copy the file from the network server to the local destination folder
    Copy-Item -Path $sourceFilePath -Destination $destinationFolderPath -Force -Verbose
    Write-Host "File downloaded successfully to $destinationFolderPath"
} else {
    Write-Host "Source file not found: $sourceFilePath"
}

# Define the source and destination paths
$sourceFilePath = "T:\RDProjects\Ohjelmistot\CoDeSys\CODESYS 64 3.5.13.0.exe"  # Replace with the actual network file path
$destinationFolderPath = "$HOME\Downloads\CODESYS 64 3.5.13.0.exe"  # Replace with the local folder where you want to save the file

# Check if the source file exists
if (Test-Path $sourceFilePath -PathType Leaf) {
    # Copy the file from the network server to the local destination folder
    Copy-Item -Path $sourceFilePath -Destination $destinationFolderPath -Force -Verbose
    Write-Host "File downloaded successfully to $destinationFolderPath"
} else {
    Write-Host "Source file not found: $sourceFilePath"
}


# Define the source and destination paths
$sourceFilePath = "T:\RDProjects\Ohjelmistot\CoDeSys\Setup_CODESYSV35SP10.exe"  # Replace with the actual network file path
$destinationFolderPath = "$HOME\Downloads\Setup_CODESYSV35SP10.exe"  # Replace with the local folder where you want to save the file

# Check if the source file exists
if (Test-Path $sourceFilePath -PathType Leaf) {
    # Copy the file from the network server to the local destination folder
    Copy-Item -Path $sourceFilePath -Destination $destinationFolderPath -Force -Verbose
    Write-Host "File downloaded successfully to $destinationFolderPath"
} else {
    Write-Host "Source file not found: $sourceFilePath"
}


# Define the source and destination paths
$sourceFilePath = "T:\RDProjects\Ohjelmistot\CoDeSys\CODESYS Safety SIL2 3.5.10.0.package"  # Replace with the actual network file path
$destinationFolderPath = "$HOME\Downloads\CODESYS Safety SIL2 3.5.10.0.package"  # Replace with the local folder where you want to save the file

# Check if the source file exists
if (Test-Path $sourceFilePath -PathType Leaf) {
    # Copy the file from the network server to the local destination folder
    Copy-Item -Path $sourceFilePath -Destination $destinationFolderPath -Force -Verbose
    Write-Host "File downloaded successfully to $destinationFolderPath"
} else {
    Write-Host "Source file not found: $sourceFilePath"
}
