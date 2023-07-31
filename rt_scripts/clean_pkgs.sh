#!/bin/sh

# Cleaning the System

# 1] Remove cache
rm -rf ~/.cache
# 2] Remove not-required old dependencies
sudo pacman -R $(pacman -Qdttq)

