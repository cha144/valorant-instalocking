import PySimpleGUI as sg
import keyboard as kb

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
                   " necessities!", font=("Valorant", 15), text_color="white", justification='center')
hotkey_button = sg.Button("Enter key to toggle instalock:", key="key")
hotkey_label = sg.Text("Current keybind: ", text_color="white"), \
    sg.Text("", font=("Valorant", 40), key="output", text_color="white")
agent_label = sg.Text("Select an agent:"), sg.Text("", font=("Valorant", 50), key="agent_output", text_color="white")

layout = [[label], [sublabel], [sg.Text("", size=(2, 1))], [hotkey_button], [sg.Text("", size=(2, 1))], [hotkey_label],
          [sg.Text("", size=(2, 1))], [agent_label],
          [astra_icon, breach_icon, brimstone_icon, chamber_icon, cypher_icon, fade_icon, gekko_icon, harbor_icon,
           jett_icon, kayo_icon],
          [killjoy_icon, neon_icon, omen_icon, phoenix_icon, raze_icon, reyna_icon, sage_icon, skye_icon, sova_icon,
           viper_icon],
          [yoru_icon]]


window = sg.Window('You nerd',
                   layout=layout,
                   font=('Valorant', 20),
                   size=(980, 700))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'key':
        key_pressed = kb.read_key()
        window["output"].update(key_pressed)
    else:
        match event:
            case "sage":
                window["agent_output"].update("Sage")
            case "astra":
                window["agent_output"].update("Astra")
            case "breach":
                window["agent_output"].update("Breach")
            case "brimstone":
                window["agent_output"].update("Brimstone")
            case "chamber":
                window["agent_output"].update("Chamber")
            case "cypher":
                window["agent_output"].update("Cypher")
            case "fade":
                window["agent_output"].update("Fade")
            case "gekko":
                window["agent_output"].update("Gekko")
            case "harbor":
                window["agent_output"].update("Harbor")
            case "jett":
                window["agent_output"].update("Jett")
            case "kayo":
                window["agent_output"].update("kayo")
            case "killjoy":
                window["agent_output"].update("Killjoy")
            case "neon":
                window["agent_output"].update("Neon")
            case "omen":
                window["agent_output"].update("Omen")
            case "phoenix":
                window["agent_output"].update("Phoenix")
            case "raze":
                window["agent_output"].update("Raze")
            case "reyna":
                window["agent_output"].update("Reyna")
            case "skye":
                window["agent_output"].update("Skye")
            case "sova":
                window["agent_output"].update("Sova")
            case "viper":
                window["agent_output"].update("Viper")
            case "yoru":
                window["agent_output"].update("Yoru")


window.close()