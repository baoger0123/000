import time
import random
food = ['滷肉飯','炒麵','炒飯','雞腿便當',
        '燙青菜','排餐','排骨便當',
        '義大利麵','牛肉麵','水餃',
        '餛飩麵','陽春麵','火鍋','壽司',
        '拉麵','定食','披薩','速食','素食','豬腳'
        ,'自助餐','港式燒臘','早午餐','稀飯','燉飯'
        ,'咖哩','乾麵','丼飯','海產','熱炒','中式料理'
        ,'咖啡廳','簡餐','無菜單料理','吃到飽','燒肉','泰式料理']
res = ['KFC','麥當勞','海底撈','必勝客','永和豆漿','達美樂','星巴克','你家附近麵攤'
       ,'爭鮮','春水堂','小蒙牛','便利商店','金色三麥','定食8','一蘭拉麵','貴族世家'
       ,'水相','你家附近夜市','義式餐廳','點點心','池上','水舞饌','麵屋一燈',
       '十二鍋','學餐','自己煮','鬍鬚張','鼎泰豐','錢都涮涮鍋','翰林茶館','築間'
       ,'王品牛排','西堤','赤鬼','美而美','古典玫瑰園','段純真牛肉麵','摩斯漢堡'
       ,'鼎王','胖老爹','21世紀','古拉爵','饗食天堂','nagi拉麵','三商巧福','拿坡里'
       ,'瓦城','屋馬燒肉','勝博殿','五花馬水餃館','四海遊龍','八方雲集',
       '吉野家','你家附近便當店']

def welcome():      #歡迎語
    print('歡迎使用“今天吃什麼”！')
    time.sleep(1)
    print('現在吃什麼呢？\n1.隨機食物\n2.隨機餐廳\n3.自己選\n4.退出')

def print_choice(a):      #選擇
    print('系統幫您選擇了%s。您滿意嗎？滿意請輸入1，不滿意請輸入2：'%a)

def end_choice(a):     #結束語
    print('您的選擇是%s,感謝使用！'%a)

def get_res():      #取得餐廳列表
    res_reserve = []
    print('輸入您想吃的三家餐廳')
    for i in range(3):
        a = input('請輸入第%s家餐廳'%(i+1))
        res_reserve.append(a)
    return(res_reserve)

welcome()
main_choice = int(input('請選擇：'))
while main_choice == 1:
    food_try = random.choice(food)
    print_choice(food_try)
    a = int(input('請選擇'))
    if a == 1:
        end_choice(food_try)
        break

while main_choice == 2:
    res_try = random.choice(res)
    print_choice(res_try)
    a = int(input('請選擇'))
    if a == 1:
        end_choice(res_try)
        break

if main_choice == 3:
    res3 = get_res()
    while True:
        res_try = random.choice(res3)
        print_choice(res_try)
        a = int(input('請選擇'))
        if a == 1:
            end_choice(res_try)
            break

elif main_choice == 4:
    end_choice('“結束”')