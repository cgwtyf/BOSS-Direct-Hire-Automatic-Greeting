import pyautogui
import pyperclip
import time
task=[{"type":"点击","content":"ipt.png"},
      {"type":"输入","content":"软件测试实习生"},
      {"type":"点击","content":"search.png"}
      ]
def mosueClick(img):
    location=pyautogui.locateCenterOnScreen(img)
    if location is not None:
        pyautogui.click(location.x,location.y,clicks=1,button="left")
        print("点击成功")
        return True
    else:
        print("未找到图片")
        return False
def doTask(task):
    if task["type"]=="点击":
        return mosueClick(task["content"])
    elif task["type"]=="输入":
        pyperclip.copy(task["content"])
        pyautogui.hotkey("ctrl","v")
        print("输入成功")
        return True

def sendMessage():
    #定位消息图标并点击
    if mosueClick("message.png"):
        time.sleep(1)
        #发消息
        pyperclip.copy("您好，请问这个岗位还有hc吗？")
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")
        time.sleep(1)
        #回到首页
        mosueClick("back.png")
        time.sleep(1)

        #定位到第一条岗位位置
        pyautogui.moveTo(540,888)
        return True
    else:
        return False

    


time.sleep(3)
while True:
    if doTask(task[0]):
        for i in range(1,3): 
            doTask(task[i])
        break
    time.sleep(1)
#获取一下第一条的坐标
# print(pyautogui.locateCenterOnScreen("location.png"))

time.sleep(1)
#移动到第一条消息处
pyautogui.moveTo(540,888)


distance=-190
while True:
    time.sleep(1)
    sendMessage()
    #     continue
    # else:
    #     #滚动鼠标滚轮，并监测消息图标
    #     pyautogui.scroll(distance)
    #     distance-=190


