#!/usr/bin/bash
# This file automates the process of pulling dependencies
#  and installing on fedora
PROJECT_DIR=$(realpath $(dirname $0)/..)
deps=(
  "perl-Expect"
  "perl-File-chdir"
  "perl-File-Find-Rule"
  "perl-Inline-Python"
  "perl-JSON"
  "perl-Net-IP"
  "perl-TOML-Parser" #Unsure
  "perl-YAML"        #Unsure
  "perl-XML-Parser"
  "grc"
  "automake"
)
sudo dnf install -y ${deps[@]}
cd $PROJECT_DIR
./autogen.sh
./configure
make
sudo make install
