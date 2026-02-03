#!/usr/bin/bash
# Create basic workflow config
TMP_DIR=$(mktemp -d)
function exit_clean() {
  rm -rf $TMP_DIR
  exit $1
}
echo "Using temp dir: $TMP_DIR"
cd $TMP_DIR
# workflow builtin start_project python-test
