#!/bin/zsh
# Script to unpublish (disable) GitHub Pages for this repository
# Requirements: GitHub CLI (gh) must be installed and authenticated

# Get repo info from git
REPO=$(git config --get remote.origin.url | sed -E 's/.*github.com[/:](.*)\.git/\1/')

if [ -z "$REPO" ]; then
  echo "Could not determine GitHub repository. Are you in a git repo?"
  exit 1
fi

echo "Disabling GitHub Pages for $REPO..."

gh api -X DELETE repos/$REPO/pages --silent
if [ $? -eq 0 ]; then
  echo "GitHub Pages disabled."
else
  echo "Failed to disable GitHub Pages."
fi

echo "Unpublish script complete."


