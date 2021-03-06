# -*- coding: utf-8 -*-

from guietta import _, ___, Gui, Quit, Exceptions
        
def user_function(a):
    return a*2

gui = Gui(
    
  [  'Enter numbers:', '__num1__' , '+' , '__num2__',   _    ],
  [  'Result:  -->'  , 'result'   , ___ ,  ___      ,   _    ],
  [  _               ,    _       ,  _  ,   _       ,  Quit  ],
  exceptions = Exceptions.POPUP)


# We can remove one of the two widgets in the "with" expression
# and the slot would be excuted only when the remaining one is triggered.

with gui.num1, gui.num2:
    gui.result = user_function(float(gui.num1) + float(gui.num2))
     
gui.run()
