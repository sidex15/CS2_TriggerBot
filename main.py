# Made by im-razvan - CS2 TriggerBot W/O Memory Writing
# Modified Code by sidex15
import pymem, pymem.process, keyboard, time
from pynput.mouse import Controller, Button
from ctypes import windll
from win32gui import GetWindowText, GetForegroundWindow
from random import uniform
from offsets import *

mouse = Controller()
client = Client()

dwEntityList = client.offset('dwEntityList')
dwLocalPlayerPawn = client.offset('dwLocalPlayerPawn')
m_iIDEntIndex = client.get('C_CSPlayerPawnBase', 'm_iIDEntIndex')
m_iTeamNum = client.get('C_BaseEntity', 'm_iTeamNum')
m_iHealth = client.get('C_BaseEntity', 'm_iHealth')

triggerKey = 0x06 #MOUSE 5
burstKey = "alt"

def get_key_state(v_key: int) -> bool:
    return bool(windll.user32.GetKeyState(v_key) & 0x80)

def main():
    print(f"[-] TriggerBot started.\n[-] Trigger key: MOUSE5\n[-] Burst key: {burstKey.upper()}")
    pm = pymem.Pymem("cs2.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    burstKeymode = False
    firemode = [0.01, 0.03]

    while True:
        try:
            if not GetWindowText(GetForegroundWindow()) == "Counter-Strike 2":
                continue

            if keyboard.is_pressed(burstKey):
                if not burstKeymode:
                    firemode[0:1] = [0.09, 0.14]
                    print("[-] Switched to Burst fire")
                    burstKeymode = not burstKeymode
                    
                else:
                    firemode[0:1] = [0.01, 0.03]
                    print("[-] Switched to Single fire")
                    burstKeymode = not burstKeymode

            if get_key_state(triggerKey):
                player = pm.read_longlong(client + dwLocalPlayerPawn)
                entityId = pm.read_int(player + m_iIDEntIndex)

                if entityId > 0:
                    entList = pm.read_longlong(client + dwEntityList)

                    entEntry = pm.read_longlong(entList + 0x8 * (entityId >> 9) + 0x10)
                    entity = pm.read_longlong(entEntry + 120 * (entityId & 0x1FF))

                    entityTeam = pm.read_int(entity + m_iTeamNum)
                    playerTeam = pm.read_int(player + m_iTeamNum)

                    if entityTeam != playerTeam:
                        entityHp = pm.read_int(entity + m_iHealth)
                        if entityHp>0:
                            time.sleep(uniform(0.01, 0.03))
                            mouse.press(Button.left)
                            time.sleep(uniform(firemode[0], firemode[1]))
                            mouse.release(Button.left)

                time.sleep(0.03)
            else:
                time.sleep(0.1)
        except KeyboardInterrupt:
            break
        except:
            pass

if __name__ == '__main__':
    main()