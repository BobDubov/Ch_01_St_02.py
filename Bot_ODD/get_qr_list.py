import subprocess
import win32gui
import win32clipboard
import time, win32com.client

# данная функция - фильтр по выбору нужного окна (по названию этого окна)
def openItNow(hwnd, windowText):
    if windowText in win32gui.GetWindowText(hwnd):
        win32gui.SetForegroundWindow(hwnd)

# Прочитать файл odd_dins.txt со списком din файлов для регистрации ОДД
with open('odd_dins.txt', 'r') as file:
    dins = file.readlines()

# список для строк с запросами регистрации
qr = []

for din in dins:
    if len(din.strip()) == 6:
        din = '0' + din.strip()
    else:
        din = din.strip()
    path = 'd:\\ONLINE_ver\\_ODD\\_RUN_\\{}.lnk'.format(din)
    subprocess.Popen(('start', path), shell = True)
    time.sleep(4)

    # выбираем среди открытых окон окно регистрации
    win32gui.EnumWindows(openItNow, 'Регистрация систем КонсультантПлюс')

    # нажимать на клавиши будет с помощью shell
    shell = win32com.client.Dispatch("WScript.Shell")

    # метод SendKeys программно нажимает на нужные клавиши
    shell.SendKeys("{RIGHT}")
    time.sleep(0.1)
    shell.SendKeys("{RIGHT}")
    time.sleep(0.1)
    shell.SendKeys("{ENTER}")
    time.sleep(0.1)

    # берем строку регистрации из буфера обмена
    win32clipboard.OpenClipboard()
    try:
        output = win32clipboard.GetClipboardData()
    except pywintypes.error:
        output = None

    shell.SendKeys("{RIGHT}")
    time.sleep(0.1)
    shell.SendKeys("{ENTER}")

    qr.append(output)
    time.sleep(0.2)



with open('qr.txt', 'w') as file:
    file.write('\n'.join(qr))