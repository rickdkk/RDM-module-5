if ! git diff --quiet --exit-code --cached; then
  echo "There are unstaged/uncommitted changes!"
else
  jb build ./ && ghp-import -n -p -f _build/html
fi