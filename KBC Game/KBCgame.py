#K.B.C Game:
print("Welcome to Game :K.B.C koun Bnega Crorepati")
print("")
Name=input("Enter your Name : ")
print("Hello",Name,"welcome to KBC Game")
print('')
#Game rules
print("There are some Game Rules:- ")
print("")
print("Rule 1. : Every question have a Four Option you can select one of them at a time. ")
print("Rule 2. : you can only answer in Capital alphabetic A,B,C,D. ")
print("Rule 3. : you can also quit the game. ")
print("Rule 4. : There will be two milestone question if you have quit the game you win milestone prize. ")
print("Rule 5. : If you crossed 2 milestones questions,they are guaranteen to win that amount Rs.10,000 and Rs.3,20,000.")
print("Rule 6. : You have two lifeline 1. 50-50 2. Hint")
print("Rule 7. : you can also quit the game. ")
print()
print('1st Qestion in screen:) ')
print()
Game=[{'Question' : 'ques1   Which of these is the name of a Zodiac sign as well as a National Award winning Hindi film actor?',
'Option':['A. Mesh','B. Dhanu','C. Mithun','D. Kumbha'],
'Answer':'C',
'50-50':['A. Mesh','C. Mithun'],
'Hint':'I am a disco dancer',
'Amount':'You win 5,000',
 'Milestone':'0'    },
{'Question': 'ques2 Which is the only one of these which comes in different sizes called mini, micro and nano?',
'Option':['A. Trucks','B. Credit cards','C. Cars','D. Sim Cards'],
'Answer':'D',
'50-50':['C. Cars','D. Sim Cards'],
'Hint':'It is use in phone ',
'Amount':'you win 10,000',
'Milestone':'you win Rs.10,000'  },
{'Question':'ques3: Which of these creatures is scientifically not classified as fish?',
'Option':['A. Rohu','B. Katla','C. Hilsa','D. Jhinga'],
'Answer':'D',
'50-50':['C. Hilsa','D. Jhinga'],
'Hint':'It is prawn or shrimp',
'Amount':'you win 20,000',
'Milestone':'0'  },
{'Question':'ques4 Which global retailer bought 77% of Flipkart for over 16 billion US Dollar in 2018?',
'Option':['A. Amazon','B. Rakuten','C. Walmart','D. Tesco'],
'Answer':'C. Walmart',
'50-50':['A. Amazon','C. Walmart'],
'Hint':'It is a mart which has walnuts',
'Amount':'you win Rs. 40,000',
'Milestone':'0'  },
{'Question':'ques5 In February 2017, ISRO created a world record by launching how many satellites through a single rocket?',
'Option':['A. 34','B. 96','C. 104','D.154'],
'Answer':'C',
'50-50':['B. 96','C. 104'],
'Hint':'It is a number for help.',
'Amount':'you win Rs. 80,000',
'Milestone':'0'  },
{'Question':'ques6 Who among the following mythological figures got his name because of his ability to move his chariot in all directions?',
'Option':['A. Adhiratha','B. Dasharatha','C. Jayadratha','D. Partha'],
'Answer':'B',
'50-50':['B. Dasharatha','C. Jayadratha'],
'Hint':'what is the father name of God ram',
'Amount':'you win Rs. 1,60,000',
'Milestone':'0'  },
{'Question':'ques7 Which is the largest joint in the human body?',
'Option':['A. Elbow','B. Hip','C. Knee','D.Shoulder'],
'Answer':'C',
'50-50':['C. Knee','D. Shoulder'],
'Hint':'we can walk with it help.',
'Amount':'you win Rs. 3,20,000',
'Milestone':'you win Rs.3,20,000'  },
{'Question':'ques8 Which Indian state had Indias first Muslim woman chief minister?',
'Option':['A. Kerala','B. Jammu & Kashmir','C. Goa','D. Assam'],
'Answer':'D',
'50-50':['C. Goa','D. Assam'],
'Hint':'It is the state of godness Kamakhya. ',
'Amount':'you win Rs. 6,40,000',
'Milestone':'0'  },
{'Question':'ques9 Common cold, polio and AIDS are diseases caused by which of these organisms?',
'Option':['A. Bacteria','B. Virus','C. Protozoa','D. Fungus'],
'Answer':'B',
'50-50':['A. Bacteria','B. Virus'],
'Hint':'it is very common diseases from 2 years ',
'Amount':'you win Rs. 12,50,000',
'Milestone':'0'  },
{'Question':'ques10 Which of these measures is the shortest in length?',
'Option':['A. Half-mile','B. Half foot','C. Half Yard','[D] Half Metre'],
'Answer':'B',
'50-50':['A. Half-mile','B. Half foot'],
'Hint':'Adha pair ',
'Amount':'you win Rs. 25,00,000',
'Milestone':'0'  },
{'Question':'ques11 Where in India is this animal found in its natural habitat?',
'Option':['A. Ranthambore National Park','B. Jim Corbett National Park','C. Gir National Park','[D] Bandipur National Park'],
'Answer':'C',
'50-50':['B. Jim Corbett National Park','C. Gir National Park'],
'Hint':'fall park',
'Amount':'you win Rs. 50,00,000',
'Milestone':'0'  },
{'Question':'ques12 In which century were the first two battles of Panipat fought?',
'Option':['A. 15th','B.16th','C. 18th','D. 17t'],
'Answer':'B',
'50-50':['A. 15th','B. 16th'],
'Hint':'International Day for the Preservation of the Ozone Layer. ',
'Amount':'you win Rs. 1crore',
'Milestone':'0'  },
{'Question':'ques13 Who wrote the Saraswati Vandana “Var de Veenavaadini var de”?',
'Option':['A. Jaishnakar Prasad','B. Sumitranandan Pant','C. Ramdhari Singh ‘Dinkar’','D. Suryakant Tripathi ‘Nirala’'],
'Answer':'D',
'50-50':['C. Ramdhari Singh ‘Dinkar’','D. Suryakant Tripathi ‘Nirala’'],
'Hint':'it is name based on sunflower ',
'Amount':'you win Rs. 5 crore',
'Milestone':'Wow !! Amzing...you win RS.5 crore'
}]
count=0
for x in Game:
  print(x['Question'])
  for y in (x['Option']):
    print(y)
  print('If you want lifeline:-       press(9)')
  print('If you want quit the Game:-  press(7)')
  ans=input('Enter your  Answer: ' )
  print("")
  sure=input('Are you sure:YES/NO :   ')
  if sure=='no':
    ans=input('Enter your answer again')
  if ans==(x['Answer']):
    print('Congratulation!!!')
    print(x['Amount'])
    print()
  elif ans=='7':
    print('Thank for coming for the game kbc')
    print(x['Amount'])
    break
  if ans=='9':
    print('chose your lifeline')
    print('1.50-50 Lifeline')
    print('2.Hint')
    ans1=input('choose a lifeline from given options: ')
    if count==2:
      print("you have used all the lifelines:")
    elif ans1=='1':
      print(x['50-50'])
      count=count+1
    elif ans1=='2':
      print(x['Hint'])
      count=count+1
    ans1=input('chose a answer : ')
    if ans1==x['Answer']:
        print('cong!!')
        print(x['Amount'])
    else:
      print(' opps!!! You are wrong')
      print('Right answer is',x["Answer"])
      print(x['Amount'])
      print(x['Milestone'])
print()
print()
print()
