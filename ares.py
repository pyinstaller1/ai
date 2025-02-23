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
import os



# left, top, width, height = 0, 0, 0, 0
che = 1000
app = None










def a01_start():
    print(7)



    print("아레스 a01_start   " + time.strftime("%H:%M", time.localtime()))



    if not gw.getWindowsWithTitle('아레스'):
        print("아레스 창이 없습니다.")
        on(0)
        return False


    """
    if len(gw.getWindowsWithTitle('아레스')) == 1:
        print("창이 1개만 있으므로 닫습니다.")
        on()
        return False
    """

        

    win = gw.getWindowsWithTitle('아레스')[0]

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



    pyautogui.moveTo(left+(width*0.5), top+(height*0.65), 2.0)   # 절전 해제
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.7), top+(height*0.65), 2.0)
    pyautogui.mouseUp()




    return True





def a01_start1():
    print("아레스 a01_start[1]   " + time.strftime("%H:%M", time.localtime()))
    
    win = gw.getWindowsWithTitle('아레스')[1]

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


    pyautogui.moveTo(left+(width*0.5), top+(height*0.65), 2.0)   # 절전 해제
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.7), top+(height*0.65), 2.0)
    pyautogui.mouseUp()

    return True













def a02_bok():
    print("아레스 a02_bok   " + time.strftime("%H:%M", time.localtime()))


    time.sleep(3)



    scr_bok = pyautogui.screenshot(region=(left + int(width*0.006), top + int(height*0.1), int(width*0.1), int(height*0.2)))
    scr_bok_np = np.array(scr_bok)
    scr_bok.save("scr_ares_bok.png")

    # 복구 ocr 탐지
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_bok_np)
    print(results[0][1])

    if results[0][1][0] != "광":
        return


    

    pyautogui.moveTo(left+(width*0.178), top+(height*0.12), 2.0)   # 복구
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(5)


    pyautogui.moveTo(left+(width*0.55), top+(height*0.73), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    



    
    pyautogui.moveTo(left+(width*0.07), top+(height*0.17), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    time.sleep(3)




    scr_map = pyautogui.screenshot(region=(left + int(width*0.417), top + int(height*0.38), int(width*0.15), int(height*0.15)))
    scr_map_np = np.array(scr_map)
    scr_map.save("scr_ares_map.png")

    # 복구 ocr 탐지
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_map_np)
    print(results[0][1])


    print(results)

    print(results[0][0][0][0])
    print(results[0][0][0][1])

    print()
    print(left + results[0][0][0][0] - (width*0.01))
    print(top+(height + results[0][0][0][1]))




    pyautogui.moveTo(left + int(width*0.417) + results[0][0][0][0] - (width*0.06), top + int(height*0.38) + results[0][0][0][1], 1.0)   # 잡화상인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()













    time.sleep(5)

    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.51), 2.0)   # 잡화상인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()




    


    time.sleep(12)


    pyautogui.moveTo(left+(width*0.9), top+(height*0.95), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.56), top+(height*0.56), 2.0)   # MAX
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.57), top+(height*0.71), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.97), top+(height*0.05), 2.0)   # X
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(1)


    pyautogui.moveTo(left+(width*0.07), top+(height*0.17), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)    

    pyautogui.moveTo(left+(width*0.03), top+(height*0.95), 2.0)   # 행성지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.7), top+(height*0.21), 2.0)   # 갈라테하빙하
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.53), top+(height*0.57), 2.0)   # 안식처
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)   

    pyautogui.moveTo(left+(width*0.65), top+(height*0.77), 2.0)   # 자동이동
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.57), top+(height*0.6), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    time.sleep(50)    

    return









def a03_jangbi():
    print("아레스 a03_jangbi   " + time.strftime("%H:%M", time.localtime()))


    pyautogui.moveTo(left+(width*0.97), top+(height*0.07), 2.0)   # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.83), top+(height*0.43), 2.0)   # 거래소
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.27), top+(height*0.158), 5.0)   # 판매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)


    
    pyautogui.moveTo(left+(width*0.27), top+(height*0.158), 5.0)   # 판매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    

    pyautogui.moveTo(left+(width*0.77), top+(height*0.95), 2.0)   # 일괄재등록
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.58), top+(height*0.627), 2.0)   # 등록
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.63), top+(height*0.95), 2.0)   # 일괄정산
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    
    

    pyautogui.moveTo(left+(width*0.95), top+(height*0.95), 2.0)   # 등록 버튼
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(1)

    # 거래소 판매 ocr 탐지
    scr_sell = pyautogui.screenshot(region=(left + int(width*0.32), top + int(height*0.25), int(width*0.17), int(height*0.08)))
    scr_sell_np = np.array(scr_sell)
    scr_sell.save("scr_ares_sell.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_sell_np)
    print(results)

    if results and ("원석" in results[0][1] or "결정" in results[0][1] or "에너지원" in results[0][1] or "설계도" in results[0][1] or "주괴" in results[0][1]):
        pyautogui.press('esc')
    else:
        pyautogui.moveTo(left+(width*0.58), top+(height*0.78), 2.0)   # 등록
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.58), top+(height*0.687), 1.0)   # 등록
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.97), top+(height*0.07), 2.0)   # 닫기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.0278), top+(height*0.738), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    




    print("거래소 완료")
    

    return





def a04_dungeon():
    print("아레스 던전   " + time.strftime("%H:%M", time.localtime()))



    pyautogui.moveTo(left+(width*0.97), top+(height*0.07), 2.0)   # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.1), top+(height*0.58), 3.0)   # 경쟁
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)

    pyautogui.moveTo(left+(width*0.38), top+(height*0.38), 2.0)   # 모리아기지
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.9), top+(height*0.95), 2.0)   # 입장
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(20)

    pyautogui.moveTo(left+(width*0.07), top+(height*0.15), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(5)

    
    pyautogui.moveTo(left+(width*0.25), top+(height*0.2587), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.3), top+(height*0.5), 2.0)   # 자동이동
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(5)





    pyautogui.moveTo(left+(width*0.87), top+(height*0.07), 2.0)   # SHOP
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(5)


    pyautogui.moveTo(left+(width*0.05), top+(height*0.95), 2.0)   # 골드일괄구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()







    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)


    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)

    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)    

    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.5), top+(height*0.88), 2.0)   # 빈칸
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()




    pyautogui.moveTo(left+(width*0.97), top+(height*0.07), 2.0)   # X
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    










    pyautogui.moveTo(left+(width*0.0278), top+(height*0.738), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()















def a05_dungeon_week():
    print("아레스 주간 던전   " + time.strftime("%H:%M", time.localtime()))


    pyautogui.moveTo(left+(width*0.97), top+(height*0.07), 2.0)   # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.1), top+(height*0.58), 3.0)   # 경쟁
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)

    pyautogui.moveTo(left+(width*0.58), top+(height*0.38), 2.0)   # 타루크기지
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.9), top+(height*0.95), 2.0)   # 입장
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(20)


    pyautogui.moveTo(left+(width*0.07), top+(height*0.15), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(5)



    # 주간 던전 지도 ocr 탐지
    scr_week = pyautogui.screenshot(region=(left + int(width*0.2), top + int(height*0.2), int(width*0.6), int(height*0.6)))
    scr_week_np = np.array(scr_week)
    scr_week.save("scr_ares_week.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_week_np)
    print(results)








    pyautogui.moveTo(left + int(width*0.2) + results[0][0][0][0] + 10, top + int(height*0.2) + results[0][0][0][1] - 10, 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()





    time.sleep(3)
    map_x = results[0][0][0][0]
    map_y = results[0][0][0][1]





    # 자동이동 ocr 탐지
    scr_move = pyautogui.screenshot(region=(int(left + int(width*0.2) + results[0][0][0][0]) + int(width*0.05), int(top + int(height*0.2) + results[0][0][0][1] + int(height*0.118)), int(width*0.1), int(height*0.1)))
    scr_move_np = np.array(scr_move)
    scr_move.save("scr_ares_move.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_move_np)
    print(results)



    pyautogui.moveTo(int(left + int(width*0.2) + results[0][0][0][0]) + int(width*0.05) + map_x + 10, int(top + int(height*0.2) + results[0][0][0][1] + int(height*0.118)) + map_y + 10, 2.0)   # 자동 이동
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.0278), top+(height*0.738), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()





    return




















def on(check):
    print("아레스 a08_kakao   " + time.strftime("%H:%M", time.localtime()))
            
    for proc in psutil.process_iter():
        if "Ares.exe" in proc.name():  # 프로세스 이름을 확인
            proc.kill()  # 강제 종료
            print("아레스 창을 닫았습니다.")
        if "ARES_Launcher.exe" in proc.name():  # 프로세스 이름을 확인
            proc.kill()  # 강제 종료
            print("ARES Launcher 창을 닫았습니다.")
                    


    time.sleep(1)


    if os.environ.get('COMPUTERNAME') == "DESKTOP-LRGAL8H":
        subprocess.Popen(r"D:\Kakaogames\ARES\ARES_Launcher.exe", shell=True)
    else:
        subprocess.Popen(r"C:\Kakaogames\ARES\ARES_Launcher.exe", shell=True)

    print("ARES Launcher 오픈")

    time.sleep(50)




    win = gw.getWindowsWithTitle('ARES Launcher')[0]


    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")


    app_kakao = Application().connect(handle=win._hWnd)
    app_kakao.window(handle=win._hWnd).set_focus()



    time.sleep(3)
    
    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.5), 2.0) # 카카오 로그인
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()

    time.sleep(1)


    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.17), 2.0) # 입력
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    if os.environ.get('COMPUTERNAME') in ["DESKTOP-LRGAL8H", "DESKTOP-792RKKB"]:
        pyautogui.write('ground077')
    else:
        pyautogui.write('ground077@naver.com')
    pyautogui.press("enter")
    

    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.3), 0.3) # 입력
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.write('windows1!')
    pyautogui.press("enter")

    time.sleep(30)


    win = gw.getWindowsWithTitle('ARES Launcher')[len(gw.getWindowsWithTitle('ARES Launcher'))-1]

    pyautogui.moveTo(win.left+(win.width*0.87), win.top+(win.height*0.78), 2.0) # 게임 실행
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(10)


    for i in range(10):
        time.sleep(60)
        if gw.getWindowsWithTitle('아레스'):
            win = gw.getWindowsWithTitle('아레스')[0]
            break


    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height


    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 점검 시작
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)




    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)
    
    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    if check==1:   # 점검이면 return
        return











    

    time.sleep(10)

    pyautogui.moveTo(left+(width*0.88), top+(height*0.738), 2.0)   # 게임 입장
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(30)


    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)

    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)    

    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)
    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 이벤트 제거
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    
    
    time.sleep(3)

    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)

    pyautogui.press('g')   # AUTO

    pyautogui.moveTo(left+(width*0.0278), top+(height*0.738), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    

    time.sleep(1)







    
    win = gw.getWindowsWithTitle('ARES Launcher')[len(gw.getWindowsWithTitle('ARES Launcher'))-1]   # 로그아웃
    app_kakao = Application().connect(handle=win._hWnd)
    app_kakao.window(handle=win._hWnd).set_focus()

    pyautogui.moveTo(win.left+(win.width*0.93), win.top+(win.height*0.08), 2.0)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')

    time.sleep(1)

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

    time.sleep(100)



    # [1] 시작
    win = gw.getWindowsWithTitle('ARES Launcher')[len(gw.getWindowsWithTitle('ARES Launcher'))-1]
    app_kakao = Application().connect(handle=win._hWnd)
    app_kakao.window(handle=win._hWnd).set_focus()
    print("아레스[1] 시작")
    
    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.5), 2.0) # 카카오 로그인
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()

    time.sleep(1)


    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.17), 2.0) # 입력
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    if os.environ.get('COMPUTERNAME') in ["DESKTOP-LRGAL8H", "DESKTOP-792RKKB"]:
        pyautogui.write('s070092@nate.com')
    else:
        pyautogui.write('s0700921@nate.com')
    pyautogui.press("enter")
    

    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.3), 0.3) # 입력
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.write('windows1!')
    pyautogui.press("enter")

    time.sleep(50)


    win = gw.getWindowsWithTitle('ARES Launcher')[len(gw.getWindowsWithTitle('ARES Launcher'))-1]

    time.sleep(1)
    
    pyautogui.moveTo(win.left+(win.width*0.87), win.top+(win.height*0.78), 2.0) # 게임 실행
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(10)



    for i in range(10):
        time.sleep(60)
        if gw.getWindowsWithTitle('아레스'):
            win = gw.getWindowsWithTitle('아레스')[0]
            break
        
    left = win.left
    top = win.top
    width = win.width
    height = win.height


    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 점검 시작
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)




    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)
    
    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(10)

    pyautogui.moveTo(left+(width*0.88), top+(height*0.738), 2.0)   # 게임 입장
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(30)


    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)

    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)    

    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)
    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 이벤트 제거
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    
    
    time.sleep(3)

    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)

    pyautogui.press('g')   # AUTO

    pyautogui.moveTo(left+(width*0.0278), top+(height*0.738), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    


    
    return















def dungeon_week_ares():
    try:
        if not a01_start():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        a05_dungeon_week()
    except Exception as e:
        print(f"아레스  a05_dungeon_week() 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        if not a01_start1():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
         a05_dungeon_week()
    except Exception as e:
        print(f"아레스  a05_dungeon_week() 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")







def dungeon_ares():
    try:
        if not a01_start():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        a04_dungeon()
    except Exception as e:
        print(f"아레스  a04_dungeon() 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        if not a01_start1():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        a04_dungeon()
    except Exception as e:
        print(f"아레스  a04_dungeon() 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")











    
def play_ares(dungeon=None):
    try:
        if not a01_start():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")
        
    try:
        a02_bok()
    except Exception as e:
        print(f"아레스 a02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        a03_jangbi()
    except Exception as e:
        print(f"아레스 a03_jangbi 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")



    try:
        if not a01_start1():
            return
    except Exception as e:
        print(f"아레스 a01_start[1] 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        a02_bok()
    except Exception as e:
        print(f"아레스 a02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        a03_jangbi()
    except Exception as e:
        print(f"아레스 a03_jangbi 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")















if __name__ == "__main__":
    # play_ares()
    on(0)
















    
