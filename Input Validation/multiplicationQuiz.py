import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,12)
    num2 = random.randint(0,12)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        #Reg ex handles correct response, block reg ex handles all incorrect responses 
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
         blockRegexes=[('.*', 'Incorrect!')],
          timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1

time.sleep(1)
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))