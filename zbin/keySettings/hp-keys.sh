
# :::key checker
# >>check key command 'xmodmap -pk'
# >>check key command 'xev'


# :::on lenovo key
# >>Hanja='keycode 105'
# >>Prtsc='keycode 107'
# >>Win_L='keycode 107'


# :::key rating up
xset r rate 250 50


# :::key swap
#setxkbmap -option 'altwin:swap_alt_win'
#setxkbmap -option 'ctrl:swapcaps'


#xmodmap -e 'keycode 105 = Control_R'
#xmodmap -e 'keycode 107 = Super_R'
#xmodmap -e 'keycode 108 = Alt_R'
#xmodmap -e 'keycode 133 = Super_R'
xmodmap -e 'keycode 9 = grave'
xmodmap -e 'keycode 49 = Escape'
