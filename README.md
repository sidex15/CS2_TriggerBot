# CS2_TriggerBot

Simple CS2 TriggerBot W/O Memory Writing
With burst fire and mouse hotkey
Added offline offets for manually updating offets

## Is it safe?
I only use it in `-insecure` flag of CS2 I only do this as my side project in game hacking.
Use at your own risk

## How to execute it?
Simply perform a `pip install -r requirements.txt` and proceed to run the Python script.

## How to Update offsets
1. Find the latest offests in this [Forum](https://www.unknowncheats.me/forum/counter-strike-2-a/576077-counter-strike-2-reversal-structs-offsets-151.html)
1. Find `dwEntityList` and `dwLocalPlayerPawn` and convert it into [decimal](https://www.rapidtables.com/convert/number/hex-to-decimal.html)
1. Once you convert it into decimal open `offets.json` and paste the new values of `dwEntityList` and `dwLocalPlayerPawn` in `"value":` variable

- UnknownCheats Release: [Here](https://www.unknowncheats.me/forum/counter-strike-2-releases/608773-cs2-triggerbot-python.html)

Developed with Python 3.11
forked from [im-razvan/CS2_TriggerBot](https://github.com/im-razvan/CS2_TriggerBot)