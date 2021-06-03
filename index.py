# 동영상 (4:50:13) 10-1.예외처리
# try:    
#     print("나누기 전용 계산기입니다.")    
#     num1 = int(input("첫 번째 숫자를 입력하세요 :"))
#     num2 = int(input("두 번째 숫자를 입력하세요 :"))
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))

# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)

# try:    
#     print("나누기 전용 계산기입니다.")    
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 :")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 :")))
#     # nums.append(int(nums[0]/nums[1]))
#     print("{} / {} = {}".format(nums[0], nums[1], nums[2]))

# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print("알 수 없는 에러가 발생하였습니다.")

# (4:58:15) 10-2.에러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 :"))
#     num2 = int(input("두 번째 숫자를 입력하세요 :"))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")

# (5:01:06) 10-3.사용자 정의 예외처리
# 사용자가 정의한 에러를 위한 클래스
# class BigNumberError(Exception):
#     # pass
#     def __init__(self, msg):
#         self.msg = msg
        
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 :"))
#     num2 = int(input("두 번째 숫자를 입력하세요 :"))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {}, {}".format(num1, num2))
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
#     print(err)

# (5:04:28) 10-4.finally
# class BigNumberError(Exception):
#     # pass
#     def __init__(self, msg):
#         self.msg = msg
        
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 :"))
#     num2 = int(input("두 번째 숫자를 입력하세요 :"))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {}, {}".format(num1, num2))
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

# (5:06:19) 10-5.퀴즈 #9
# 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
         # 출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#        치킨 소진시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#        출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# 나의 답변
# class SoldOutError(Exception):
#     pass
    
# #     def __init__(self, msg):
# #         self.msg = msg
    
# #     def __str__(self):
# #         return self.msg

# try:
#     chicken = 10
#     waiting = 1
#     while(True):
#         print("[남은치킨 : {}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))    
#         if order < 0:
#             raise ValueError
#         if order > chicken:
#             print("재료가 부족합니다.")
#             raise SoldOutError              
#         else:
#             print("[대기번호 {}] {} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order            
# except ValueError:
#     print("잘못된 값을 입력하였습니다.")
# except SoldOutError:
#     print("재고가 소진되어 더 이상 주문을 받지 않습니다.")

# 나도코딩님 답변
# class SoldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print("[남은치킨 : {}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))    
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {}] {} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order            
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

# (5:14:23) 11-1.모듈

# import theather_module
# theather_module.price(3)
# theather_module.price_morning(4)
# theather_module.price_soldier(5)

# import theather_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theather_module import *

# price(3)
# price_morning(4)
# price_soldier(5)

# from theather_module import price, price_morning

# price(5)
# price_morning(6)
# price_soldier(7)

# from theather_module import price_soldier as price
# price(5)

# (5:24:10) 11-2.패키지
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# (5:30:30) 11-3._all_
# from random import *

# from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# # (5:34:16) 11-4.모듈 직접 실행
# from travel import *
# # # trip_to = vietnam.VietnamPackage()
# # trip_to = thailand.ThailandPackage()
# # trip_to.detail()

# # (5:37:00) 11-5.패키지, 모듈 위치
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# (5:40:33) 11-6.pip install

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# (5:46:04) 11-7.내장함수
# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print('{}은 아주 좋은 언어입니다.'.format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고  있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))

# lst = [1,2,4]
# print(dir(lst))

# name = "jim"
# print(dir(name))

# (5:50:38) 11-8.외장함수
# glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py 인 모든  파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# # print("오늘 날짜는", datetime.date.today())

# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은", today + td)

# (5:58:49) 11-9.퀴즈 #10
# 프로젝트 내에 나만의  시그니처를 남기는 모듈을 만드시오
# 조건 : 모듈 파일명은 byme.py 로 작성
# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력예제)
# 이 프로그램은 나도코딩에 의해 만들어졌습니다.
# 유튜브 : http://youtube.com
# 이메일 : nadocoding@gmail.com

# (6:01:08) 12.Outro
