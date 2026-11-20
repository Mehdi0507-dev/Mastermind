import random

def make_secret():    #ساخت کد مخفی شامل ۴ عدد غیر تکراری
    secret = []
    while len(secret) < 4:
        n = random.randint(1,6)
        if n not in secret:
            secret.append(n)
    return secret

def check_input(guess):            #بررسی معتبر بودن ورودی کاربر
    if len(guess) != 4:
        return False

    for ch  in guess:
        if ch < '1' or ch > '6':
            return False

    if len(set(guess)) != 4:
        return False

    return True

def chech_guess(secret,guess):      #مقایسه حدس کاربر با کد مخفی
    correct_place = 0
    wrong_place = 0

#مقایسه تک تک ارقام حدس با کد مخفی
    for i in range(4):

        #بررسی درست بودن عدد و جایگاه ان
        if int(guess[i]) == secret[i]:
            correct_place += 1

            #بررسی وجود عدد در کد مخفی در جایگاه اشتباه
        elif int(guess[i]) in secret:
            wrong_place += 1

    return correct_place,wrong_place

def play_game():        #تابع اصلی اجرای برنامه
    print("welcome to Mastermind Game")
    print("==========================")
    print("programmer:mohammad mehdi Rahimi")
    print("==========================")

    #تولید کد مخفی و مقداردهی اولیه فرصت ها
    secret = make_secret()
    attempt = 0

    #اجرای بازی با حداکثر ۱۰ فرصت
    while attempt < 10 :

        #دریافت حدس از کاربر
        guess = input("guess your guess(4 digits from 1 to 6): ")
        #بررسی اعتبار ورودی کاربر

        if not check_input(guess):
            print("invalid input,please try again")
            continue

         #تبدیل رشته ورودر به لیست اعداد
        guess = [int(ch) for ch in guess]
        print(guess)
            #کم کردن یک فرصت برای حدس معتبر

        attempt += 1
         #مقایسه حدس کاربر با کد مخفی

        correct,wrong = chech_guess(secret,guess)

        print("correct digits in correct place", correct)
        print("correct digits in wrong place", wrong)
        print("remaining attemps",10 - attempt)

        #بررسی برنده شدن کاربر
        if correct == 4:
            print("you win")
            print("number of attempts",attempt)
            return
         #پایان بازی در صورت تمام شدن فرصت ها
    print("Game over")
    print("secret code was",secret)

#شروع بازی
play_game()




