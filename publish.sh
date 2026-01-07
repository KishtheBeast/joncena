# Add, commit, and push changes
git add .
git commit -m "Automated publish"
git push

echo "Re-enabling GitHub Pages for $REPO (source: main branch, root path)..."
gh api -X POST repos/$REPO/pages --field source[branch]=main --field source[path]=/
if [ $? -eq 0 ]; then
  echo "GitHub Pages re-enabled for GitHub Actions (main branch, root path)."
else
  echo "Failed to re-enable GitHub Pages. You may need to enable it manually in repository settings."
fi


