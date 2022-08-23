#!/bin/bash

plan='/path/to/plan/__PLAN__.md'
grep $(date +%b) $plan | awk '{$(NF--)=""; print}'

