#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias py='python'
alias ls='ls --color=auto'
alias config='code ~/Code/config.code-workspace'
PS1='\[\033[01;36m\]┌──\[\033[01;35m\] <\u㉿\h> \[\033[01;36m\][\W]\n└─> \[\033[00m\]'

# run this everytime we open up a new terminal
neofetch
. "$HOME/.cargo/env"
