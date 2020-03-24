"""Question Ripper"""
'''Pulls questions from subreddit list
Appends them to the queue file (questions.txt)
Appends them to the the usedQuestion file (usedQuestions.txt)'''

import praw

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
find('.\subreddits.txt', subreddits)
print('Subreddits found\n')

print('Finding banned words...')
find('bannedWords.txt', bannedWords)
print('Banned words found\n')

print('Finding used questions...')
find('usedQuestions', usedQuestions)
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
    print(str(round(((subNumber/subreddits.__len__())*100), 2)) + '%')

print(str(len(pulls)) + ' of the questions pulled passed filters')

# Counts number of unused questions
for pull in pulls:
    if pull not in usedQuestions:
        count += 1

# Adds questions to queue file
for pull in pulls:
    if pull not in usedQuestions:
        f = open(".\Questions", "a")
        f.write(pull + "\n")
        f.close()

print('\nAdded questions to Questions.txt')

# Adds questions to used question file
for pull in pulls:
    if pull not in usedQuestions:
        f = open(".\usedQuestions", "a")
        f.write(pull + "\n")
        f.close()

print('\nAdded questions to usedQuestions.txt')
print('\nAdded ' + str(count) + ' questions to the queue')
