## {{ ansible_managed }}

## /etc/profile.d/bash_history_timestamp.sh - configure Bash to display timestamps for each command, displayed in history. Yay.

## Default is yyyy-mm-dd HH:mm:SS
export HISTTIMEFORMAT="%F %T "

## Set the history size to something decent
export HISTSIZE=10000
export HISTFILESIZE=10000

## By default, commands starting with white space are not saved in the history.  Personally, I find this useful.
## If however you want all commands logged, then uncomment/set these two environment variables..
#export HISTCONTROL=""
#export HISTIGNORE=""

## End of file
