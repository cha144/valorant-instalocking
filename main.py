import PySimpleGUI as sg
import keyboard as kb
import mouse
import pyautogui
import time

# Declare agent icons
sage_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Sage_icon.png", key="sage")
astra_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Astra_icon.png", key="astra")
breach_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Breach_icon.png", key="breach")
brimstone_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Brimstone_icon.png", key="brimstone")
chamber_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Chamber_icon.png", key="chamber")
cypher_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Cypher_icon.png", key="cypher")
fade_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Fade_icon.png", key="fade")
gekko_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Gekko_icon.png", key="gekko")
harbor_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Harbor_icon.png", key="harbor")
jett_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Jett_icon.png", key="jett")
kayo_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/KAYO_icon.png", key="kayo")
killjoy_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Killjoy_icon.png", key="killjoy")
neon_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Neon_icon.png", key="neon")
omen_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Omen_icon.png", key="omen")
phoenix_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Phoenix_icon.png", key="phoenix")
raze_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Raze_icon.png", key="raze")
reyna_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Reyna_icon.png", key="reyna")
skye_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Skye_icon.png", key="skye")
sova_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Sova_icon.png", key="sova")
viper_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Viper_icon.png", key="viper")
yoru_icon = sg.Button(image_filename="valorant-agent-icons/1679171250868/Yoru_icon.png", key="yoru")

sg.theme('Black')
label = sg.Text("Valorant Instalock Resource", font=("Valorant",40) ,text_color="white", justification='center')
sublabel = sg.Text("The all complete tool you need for your instalock"
                   " necessities!", font=("Valorant", 15),
                   text_color="white", justification='center')
subsublabel = sg.Text("(Positions your mouse to the desired agent) "
                      "Requires 1920x1080 resolution and all agents unlocked.", font=("Valorant", 12),
                      text_color="white", justification='center')
hotkey_button = sg.Button("Enter key to toggle instalock:", key="key")
hotkey_label = sg.Text("Current keybind: ", text_color="white"), \
    sg.Text("", font=("Valorant", 40), key="output", text_color="white")
agent_label = sg.Text("Select an agent:"), sg.Text("", font=("Valorant", 50), key="agent_output", text_color="white")

layout = [[label], [sublabel], [subsublabel], [sg.Text("", size=(2, 1))], [hotkey_button], [sg.Text("", size=(2, 1))], [hotkey_label],
          [sg.Text("", size=(2, 1))], [agent_label],
          [astra_icon, breach_icon, brimstone_icon, chamber_icon, cypher_icon, fade_icon, gekko_icon, harbor_icon,
           jett_icon, kayo_icon],
          [killjoy_icon, neon_icon, omen_icon, phoenix_icon, raze_icon, reyna_icon, sage_icon, skye_icon, sova_icon,
           viper_icon],
          [yoru_icon]]


window = sg.Window('You nerd',
                   layout=layout,
                   font=('Valorant', 20),
                   size=(980, 730))

mouseX = 0
mouseY = 0

def hotkey_pressed():
    print(mouse.get_position())
    pyautogui.moveTo(mouseX, mouseY)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'key':
        key_pressed = kb.read_key()
        window["output"].update(key_pressed)
        kb.add_hotkey(key_pressed, hotkey_pressed)
    else:
        match event:
            case "sage":
                window["agent_output"].update("Sage")
            case "astra":
                window["agent_output"].update("Astra")
                mouseX = 539
                mouseY = 918
            case "breach":
                window["agent_output"].update("Breach")
                mouseX = 622
                mouseY = 918
            case "brimstone":
                window["agent_output"].update("Brimstone")
                mouseX = 717
                mouseY = 918
            case "chamber":
                window["agent_output"].update("Chamber")
                mouseX = 786
                mouseY = 918
            case "cypher":
                window["agent_output"].update("Cypher")
                mouseX = 876
                mouseY = 918
            case "fade":
                window["agent_output"].update("Fade")
                mouseX = 960
                mouseY = 918
            case "gekko":
                window["agent_output"].update("Gekko")
                mouseX = 1044
                mouseY = 918
            case "harbor":
                window["agent_output"].update("Harbor")
                mouseX = 1122
                mouseY = 918
            case "jett":
                window["agent_output"].update("Jett")
                mouseX = 1212
                mouseY = 918
            case "kayo":
                window["agent_output"].update("kayo")
                mouseX = 1287
                mouseY = 918
            case "killjoy":
                window["agent_output"].update("Killjoy")
                mouseX = 1380
                mouseY = 918
            case "neon":
                window["agent_output"].update("Neon")
                mouseX = 546
                mouseY = 1000
            case "omen":
                window["agent_output"].update("Omen")
                mouseX = 626
                mouseY = 1000
            case "phoenix":
                window["agent_output"].update("Phoenix")
                mouseX = 717
                mouseY = 1000
            case "raze":
                window["agent_output"].update("Raze")
                mouseX = 797
                mouseY = 1000
            case "reyna":
                window["agent_output"].update("Reyna")
                mouseX = 872
                mouseY = 1000
            case "skye":
                window["agent_output"].update("Skye")
                mouseX = 969
                mouseY = 1000
            case "sova":
                window["agent_output"].update("Sova")
                mouseX = 1040
                mouseY = 1000
            case "viper":
                window["agent_output"].update("Viper")
                mouseX = 1132
                mouseY = 1000
            case "yoru":
                window["agent_output"].update("Yoru")
                mouseX = 1221
                mouseY = 1000
    time.sleep(0.3)
window.close()