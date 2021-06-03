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

try:    
    print("나누기 전용 계산기입니다.")    
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 :")))
    nums.append(int(input("두 번째 숫자를 입력하세요 :")))
    # nums.append(int(nums[0]/nums[1]))
    print("{} / {} = {}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except:
    print("알 수 없는 에러가 발생하였습니다.")

# (4:58:15) 10-2.에러 발생시키기
