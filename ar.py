import time
import pygetwindow as gw
from pywinauto import Application
import pyautogui
import numpy as np
import cv2
import easyocr
import re
import psutil
import subprocess



left, top, width, height = 0, 0, 0, 0
che = 1000
wins = None
app = None










def a01_start():
    print("아스달 a01_start   " + time.strftime("%H:%M", time.localtime()))


    flag_start = False
    if not gw.getWindowsWithTitle('Arthdal Chronicles'):
        print("아스달 창이 없습니다.")
        a08_netmarble()
        flag_start = True

        

    win = gw.getWindowsWithTitle('Arthdal Chronicles')[0]

    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")

    global app
    app = Application().connect(handle=win._hWnd)

    if not (app.window(handle=win._hWnd).is_enabled() and app.window(handle=win._hWnd).is_visible()):
        print("창이 비활성화되어 있거나 보이지 않습니다.")
        return False

    try:
        app.window(handle=win._hWnd).set_focus()
    except RuntimeError as e:
        print(f"Error: {e}")
        return False


    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height

    if flag_start:
        print("아스달 시작")

        pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        time.sleep(30)


        pyautogui.moveTo(left+(width*0.5), top+(height*0.38), 2.0)   # 서버 선택
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        time.sleep(60)

        pyautogui.moveTo(left+(width*0.838), top+(height*0.238), 1.0)   # X
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()
        

        pyautogui.moveTo(left+(width*0.838), top+(height*0.938), 1.0)   # 게임 시작
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        time.sleep(30)


        return True



    # 절전 화면 해제
    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.8), top+(height*0.5), 2.0)
    pyautogui.mouseUp()

    time.sleep(2)
    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.75), 3.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    return True




def a02_jangbi():
    print("아스달 a02_jangbi   " + time.strftime("%H:%M", time.localtime()))


    pyautogui.moveTo(left+(width*0.93), top+(height*0.07), 2.0)   # 가방
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.93), top+(height*0.93), 2.0)   # 분해
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    
    pyautogui.moveTo(left+(width*0.78), top+(height*0.93), 2.0)   # 자동선택
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.78), top+(height*0.2), 1.0)   # 장비
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.83), top+(height*0.2), 1.0)   # 장비
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.87), top+(height*0.2), 1.0)   # 장비
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.38), top+(height*0.93), 2.0)   # 분해
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()    

    pyautogui.moveTo(left+(width*0.57), top+(height*0.6), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    time.sleep(2)


    pyautogui.moveTo(left+(width*0.57), top+(height*0.6), 2.0)   # 빈공간터치
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()    

    pyautogui.moveTo(left+(width*0.957), top+(height*0.07), 2.0)   # 종료
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    print("장비 분해 완료")





def a03_bok():
    print("아스달 a03_bok   " + time.strftime("%H:%M", time.localtime()))

    time.sleep(1)



    scr_bok = pyautogui.screenshot(region=(left + int(width*0.083), top + int(height*0.23), int(width*0.15), int(height*0.25)))
    scr_bok_np = np.array(scr_bok)
    scr_bok.save("scr_ar_bok.png")

    # 복구 ocr 탐지
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_bok_np)
    print(results)
    
    if results and results[0][1].startswith(("잡", "집")):
        print("복구")

        pyautogui.moveTo(left+(width*0.0388), top+(height*0.14), 2.0)   # 복구
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        scr_bok_check = pyautogui.screenshot(region=(left + int(width*0.53), top + int(height*0.75), int(width*0.2), int(height*0.1)))
        scr_bok_check_np = np.array(scr_bok_check)
        scr_bok_check.save("scr_ar_bok_check.png")

        reader = easyocr.Reader(['ko', 'en'], gpu=False)
        results = reader.readtext(scr_bok_check_np)
        print(results)

        if results and results[0][1].startswith(("복")):

            pyautogui.moveTo(left+(width*0.58), top+(height*0.78), 2.0)   # 복구
            pyautogui.mouseDown()
            time.sleep(1)
            pyautogui.mouseUp()

            pyautogui.moveTo(left+(width*0.58), top+(height*0.63), 2.0)   # 확인
            pyautogui.mouseDown()
            time.sleep(1)
            pyautogui.mouseUp()

        else:
            pyautogui.press("esc")   # esc 키


        print("잡화 상인에게로 이동")


        pyautogui.moveTo(left+(width*0.1), top+(height*0.23), 2.0)   # 잡화 상인
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.38), top+(height*0.6), 2.0)   # 걸어서 이동
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        time.sleep(30)

        pyautogui.moveTo(left+(width*0.2), top+(height*0.38), 2.0)   # 중형 회복 물약
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.587), top+(height*0.65), 2.0)   # MAX
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.587), top+(height*0.75), 2.0)   # 구매
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.0388), top+(height*0.07), 2.0)   # 뒤로
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.9), top+(height*0.338), 2.0)   # 빠른 사냥터
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.9), top+(height*0.15), 2.0)   # 빠른 사냥터
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.9), top+(height*0.338), 2.0)   # 빠른 사냥터
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.9), top+(height*0.15), 2.0)   # 빠른 사냥터
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.9), top+(height*0.338), 2.0)   # 빠른 사냥터
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.9), top+(height*0.15), 2.0)   # 빠른 사냥터
        pyautogui.mouseUp()    

        pyautogui.moveTo(left+(width*0.9), top+(height*0.338), 2.0)   # 빠른 사냥터
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.9), top+(height*0.15), 2.0)   # 빠른 사냥터
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.9), top+(height*0.338), 2.0)   # 빠른 사냥터
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.9), top+(height*0.15), 2.0)   # 빠른 사냥터
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.9), top+(height*0.338), 2.0)   # 빠른 사냥터
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.9), top+(height*0.15), 2.0)   # 빠른 사냥터
        pyautogui.mouseUp()    

        pyautogui.moveTo(left+(width*0.9), top+(height*0.338), 2.0)   # 빠른 사냥터
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.9), top+(height*0.15), 2.0)   # 빠른 사냥터
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.9), top+(height*0.338), 2.0)   # 빠른 사냥터
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.9), top+(height*0.15), 2.0)   # 빠른 사냥터
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.9), top+(height*0.338), 2.0)   # 빠른 사냥터
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.9), top+(height*0.15), 2.0)   # 빠른 사냥터
        pyautogui.mouseUp()    

        pyautogui.moveTo(left+(width*0.9), top+(height*0.338), 2.0)   # 빠른 사냥터
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.9), top+(height*0.15), 2.0)   # 빠른 사냥터
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.9), top+(height*0.338), 2.0)   # 빠른 사냥터
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()
    

        pyautogui.moveTo(left+(width*0.38), top+(height*0.6), 2.0)   # 걸어서 이동
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()















def a08_netmarble():
    print("아스달 a08_netmarble   " + time.strftime("%H:%M", time.localtime()))
    
    # for win in gw.getAllWindows():
    #    print(win.title)

    if gw.getWindowsWithTitle('NetmarbleLauncher'):
        win = gw.getWindowsWithTitle('NetmarbleLauncher')[0]
    else:
        print("NetmarbleLauncher 열기")
        ######  NetmarbleLauncher 여는 로직 ###########
        return


    print(win.title)
    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")

    
    app_response = Application().connect(handle=win._hWnd)
    app_response.window(handle=win._hWnd).set_focus()

    left_response = win.left
    top_response = win.top
    width_response = win.width
    height_response = win.height

    pyautogui.moveTo(left_response+(width_response*0.8), top_response+(height_response*0.9), 2.0) # 플레이
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(60)



    """
    time.sleep(3)


    pyautogui.moveTo(left_response+(width_response*0.5), top_response+(height_response*0.45), 2.0) # 넷마블 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    
    pyautogui.moveTo(left_response+(width_response*0.5), top_response+(height_response*0.43), 2.0) # 넷마블 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.write("ground077@naver.com")


    pyautogui.moveTo(left_response+(width_response*0.5), top_response+(height_response*0.50), 2.0) # 넷마블 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.write("windows1!")


    pyautogui.moveTo(left_response+(width_response*0.5), top_response+(height_response*0.57), 2.0) # 넷마블 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)

    pyautogui.moveTo(left_response+(width_response*0.8), top_response+(height_response*0.9), 2.0) # 플레이
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)
    """




















    
def play_ar():
    try:
        if not a01_start():
            return
    except Exception as e:
        print(f"아스달 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        a02_jangbi()
    except Exception as e:
        print(f"아스달 a02_jangbi 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        a03_bok()
    except Exception as e:
        print(f"아스달 a03_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")





    pyautogui.moveTo(left+(width*0.038), top+(height*0.61), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


if __name__ == "__main__":
    play_ar()















    
