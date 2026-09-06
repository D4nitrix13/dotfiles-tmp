-- http://projects.haskell.org/xmobar/

Config { 
    font = "xft:UbuntuMono Nerd Font:weight=bold:style=italic:pixelsize=22:antialias=true:hinting=true",
    bgColor = "#292d3e",
    fgColor = "#f07178",
    lowerOnStart = True,
    hideOnStart = False,
    allDesktops = True,
    persistent = True,
    commands = [
        -- 󰃰: nf-md-calendar_clock
        -- : nf-oct-cpu
        -- : nf-fa-download
        Run Date "󰃰 %A, %d of %B %Y - %I:%M:%S %p" "date" 1,
        Run Com "pamixer" [ "--get-volume-human" ] "volume" 1,
        
        Run Com "battery" [] "battery" 600,
        Run Com "brightness" [] "brightness" 10,
        
        Run Network "enp10s0" ["-t", " <rx>kb  <tx>kb"] 150,
        Run Cpu ["-t", " (<total>%)","-H","50","--high","red"] 150,
        Run Memory ["-t", "  <used>M (<usedratio>%)"] 150,

        Run Com "bash" ["-c", "checkupdates | wc -l"] "updates" 60,
        Run Com "/home/d4nitrix13/.config/xmobar/trayer-padding-icon.sh" [] "trayerpad" 600,
        Run UnsafeStdinReader
    ],
    alignSep = "}{",
    template = "<fc=#b303ff>   </fc>%UnsafeStdinReader% }{ \
        \<fc=#e1acff>  %updates% </fc>\
        \<fc=#82AAFF>  %volume% </fc>\
        \<fc=#FFB86C> %cpu% </fc>\
        \<fc=#FF5555> %memory% </fc>\
        \<fc=#c3e88d> %enp10s0% </fc>\
        \<fc=#8BE9FD> %date% </fc>\
        \%trayerpad%"
}
