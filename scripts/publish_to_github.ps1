# Requires Git + GitHub CLI (gh) and your explicit authentication.
# Run this from the extracted repository directory in PowerShell.
$ErrorActionPreference = 'Stop'
gh auth status
if (-not (Test-Path '.git')) { git init -b main }
git add .
git commit -m 'Add verified bibliographic tables, manuscript, and Zenodo metadata'
gh repo create zaher1976/SRS-to-Agile-User-Stories-SLR --public --source . --remote origin --push --description 'PRISMA-informed SRS-to-Agile User Stories evidence review and reproducibility tables'
Write-Host 'Next: enable the repository in Zenodo, then create a GitHub release.'
