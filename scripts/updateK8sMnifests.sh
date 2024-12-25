#!/bin/bash
set -x
REPO_URL="https://Bvyn3laGEmdLhyy3hK2UCBMf7b1GjIuGhbB0PKTUrSUKV7yBXASRJQQJ99ALACAAAAAAAAAAAAASAZDOyjNh@dev.azure.com/sparshwadhwadevops/voteapp/_git/voteapp"
git clone "$REPO_URL" /tmp/temp_repo
cd /tmp/temp_repo
sed -i "s|image:.*|image: resumecr.azurecr.io/$2:$3|g" k8s-specifications/$1-deployment.yaml
git add .
git commit -m "update K8s Manifests"
git push
rm -rf /tmp/temp_repo
