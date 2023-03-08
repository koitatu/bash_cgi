#/bin/bash

$LOG_FILE="/var/www/html/output/dump_$(date +%Y%m%d')_$txt"
echo $(date +%Y-%m-%d') $0 $@ |tee -a LOG_FILE
