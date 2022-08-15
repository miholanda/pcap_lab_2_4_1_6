""" LAB

Estimated time
30 minutes

Level of difficulty
Medium

Objectives
improving the student's skills in user_numerating with strings;
using strings to represent non-text data.
Scenario
You've surely seen a seven-segment display.

It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful.

Test data
Sample input:

123

Sample output:

  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 

Sample input:

9081726354

Sample output:

### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   #  """

while True:
  dict_numeros = {
      '1': ('  #', ' ##', '# #', '  #', '  #'), 
      '2': ('###', '  #', '###', '#  ', '###'),
      '3': ('###', '  #', '###', '  #', '###'),
      '4': ('# #', '# #', '###', '  #', '  #'),
      '5': ('###', '#  ', '###', '  #', '###'),
      '6': ('###', '#  ', '###', '# #', '###'),
      '7': ('###', '  #', '  #', '  #', '  #'),
      '8': ('###', '# #', '###', '# #', '###'),
      '9': ('###', '# #', '###', '  #', '###'),
      '0': ('###', '# #', '# #', '# #', '###')}
  '''
  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###}
  '''
  user_num = int(input("Informe um numero ou 0 para sair: "))
  if  user_num == 0:
    print("Bubye!!! \n")
    break
  else:
    for tamanho in range(len(dict_numeros['1'])):
      temp_line = []
      for i in  str(user_num):
        temp_line.append(dict_numeros[i][tamanho])
      print(' '.join(temp_line))
        




  

