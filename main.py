import pyautogui
import time
import pyscreenshot as ImageGrab
import praw

pyautogui.PAUSE = 1

pyautogui.FAILSAFE = False

width, height = pyautogui.size()
print("The screen size is " + str(width) + "x" + str(height))

questions = []

questionNumber = 0

detectionInterval = 20

time.sleep(1)

totalCount = 0
postCount = 100

while totalCount < postCount:

    '''MARK:// Declarations'''

    count = 0

    usable = True

    subNumber = 0

    reddit = praw.Reddit(client_id='DPpm4n7MnGF3gA',
                         client_secret='8j0anl0eeWKG9x79p_kX5u3qfU4',
                         user_agent='macOs:com.example.test:v0.1')

    print('\nRead only mode initialized correctly: ' + str(reddit.read_only) + '\n')

    usedQuestions = []

    bannedWords = []

    pulls = []

    subreddits = []


    def find(path, append):
        with open(path) as f:
            file = f.readlines()
        for item in file:
            # index = file.index(item)
            item = item.strip()
            append.append(item)


    '''MARK:// Script'''

    # Pulls in all the necessary files
    print('Finding subreddits...')
    find('/Users/blakebollinger/Library/Mobile Documents/com~apple~CloudDocs/Projects/Quora Bot/venv/Text Files/subreddits.txt', subreddits)
    print('Subreddits found\n')

    print('Finding banned words...')
    find('/Users/blakebollinger/Library/Mobile Documents/com~apple~CloudDocs/Projects/Quora Bot/venv/Text Files/bannedWords.txt', bannedWords)
    print('Banned words found\n')

    print('Finding used questions...')
    find('/Users/blakebollinger/Library/Mobile Documents/com~apple~CloudDocs/Projects/Quora Bot/venv/Text Files/usedQuestions.txt', usedQuestions)
    print('Used questions found\n\nPulling questions...')

    # Pulls questions and passes them through the filters
    for sub in subreddits:
        for post in reddit.subreddit(sub).hot(limit=100000):
            if "?" in post.title.lower() and len(post.title) > 20:
                for ban in bannedWords:
                    if ban in post.title.lower():
                        usable = False
                if usable:
                    pulls.append(post.title)
                else:
                    usable = True
        subNumber += 1
        print(str(round(((subNumber / subreddits.__len__()) * 100), 2)) + '%')

    print(str(len(pulls)) + ' of the questions pulled passed filters')

    # Counts number of unused questions
    for pull in pulls:
        if pull not in usedQuestions:
            count += 1

    # Adds questions to queue file
    for pull in pulls:
        if pull not in usedQuestions:
            f = open("/Users/blakebollinger/Library/Mobile Documents/com~apple~CloudDocs/Projects/Quora Bot/venv/Text Files/Questions.txt", "a")
            f.write(pull + "\n")
            f.close()

    print('\nAdded questions to Questions.txt')

    # Adds questions to used question file
    for pull in pulls:
        if pull not in usedQuestions:
            f = open("/Users/blakebollinger/Library/Mobile Documents/com~apple~CloudDocs/Projects/Quora Bot/venv/Text Files/usedQuestions.txt", "a")
            f.write(pull + "\n")
            f.close()

    print('\nAdded questions to usedQuestions.txt')


    print('\nAdded ' + str(count) + ' questions to the queue')

    questions = []

    # open file and read the content in a list
    file = open('/Users/blakebollinger/Library/Mobile Documents/com~apple~CloudDocs/Projects/Quora Bot/venv/Text Files/Questions.txt', 'r')
    for line in file:
        # remove linebreak which is the last character of the string
        appendingQuestion = line[:-1]

        # add item to the list
        questions.append(appendingQuestion)

    file.close()

    while len(questions) > 0 and totalCount < postCount:

        totalCount += 1

        time.sleep(5)

        questions = []

        # open file and read the content in a list
        file = open('/Users/blakebollinger/Library/Mobile Documents/com~apple~CloudDocs/Projects/Quora Bot/venv/Text Files/Questions.txt', 'r')
        for line in file:
            # remove linebreak which is the last character of the string
            appendingQuestion = line[:-1]

            # add item to the list
            questions.append(appendingQuestion)

        file.close()

        # Click Add New Question
        pyautogui.click(700, 260)

        time.sleep(.5)

        # Type question
        pyautogui.typewrite(questions[0], interval=0.05)

        time.sleep(.5)

        r,g,b = 0,0,0
        y = 550
        im = ImageGrab.grab(bbox=(1017, y, 1018, y+1))  # X1,Y1,X2,Y2

        rgb_im = im.convert('RGB')
        r, g, b = rgb_im.getpixel((0, 0))

        while r != 46 or g != 105 or b != 255:
            im = ImageGrab.grab(bbox=(1017, y, 1018, y+1))  # X1,Y1,X2,Y2
            rgb_im = im.convert('RGB')
            r, g, b = rgb_im.getpixel((0, 0))
            y += 20
            if r == 0 and g == 0 and b == 0:
                pyautogui.press('enter')
                break
            print(r,g,b,y)

        pyautogui.click(1017, y)

        time.sleep(3)


        r,g,b = 0,0,0
        y = 475
        im = ImageGrab.grab(bbox=(998, y, 999, y+1))  # X1,Y1,X2,Y2

        rgb_im = im.convert('RGB')
        r, g, b = rgb_im.getpixel((0, 0))

        while r != 46 or g != 105 or b != 255:
            im = ImageGrab.grab(bbox=(998, y, 999, y+1))  # X1,Y1,X2,Y2
            rgb_im = im.convert('RGB')
            r, g, b = rgb_im.getpixel((0, 0))
            y += 20
            if r == 0 and g == 0 and b == 0:
                pyautogui.PAUSE = 0.1
                pyautogui.click(1020, 520)
                pyautogui.click(1020, 540)
                pyautogui.click(1020, 560)
                pyautogui.click(1020, 580)
                pyautogui.click(1020, 600)
                pyautogui.click(1020, 620)
                pyautogui.click(1020, 640)
                pyautogui.click(1020, 660)
                pyautogui.click(1020, 680)
                pyautogui.click(1020, 700)
                pyautogui.click(1020, 720)
                pyautogui.click(1020, 740)
                pyautogui.click(1020, 760)
                pyautogui.PAUSE = 1
                break
            print(r,g,b,y)

        pyautogui.click(998, y)

        time.sleep(3)

        # Click X
        pyautogui.click(1070, 255)

        time.sleep(.5)

        # Click Ok
        pyautogui.keyDown('enter')
        time.sleep(.25)
        pyautogui.keyUp('enter')

        pyautogui.click(200, 80)

        pyautogui.typewrite('quora.com', interval=0.05)

        pyautogui.press('enter')

        f = open('venv/Text Files/Questions.txt', 'r' )
        remainingQuestions = f.readlines()
        f.close()

        remainingQuestions = remainingQuestions[1:]

        f = open('venv/Text Files/Questions.txt', 'w' )
        for question in remainingQuestions:
            f.write(question)
        f.close()
