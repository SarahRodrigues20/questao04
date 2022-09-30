num1  =  int ( input ( "Digite um primeiro número: " ))
num2  =  int ( input ( "Digite um segundo número: " ))
num3  =  int ( input ( "Digite um terceiro número: " ))

if  num1  <=  num2  e  num1  <=  num3  e  num2  <=  num3 :
    print ( f"A ordem crescente é { num1 } , { num2 } e { num3 } " )
elif  num1  <=  num2  e  num1  <=  num3  e  num3  <=  num2 :
    print ( f"A ordem crescente é { num1 } , { num3 } e { num2 } " )
elif  num2  <=  num1  e  num2  <=  num3  e  num1  <=  num3 :
    print ( f"A ordem crescente é { num2 } , { num1 } e { num3 } " )
elif  num2  <=  num1  e  num2  <=  num3  e  num3  <=  num1 :
    print ( f"A ordem crescente é { num2 } , { num3 } e { num1 } " )
elif  num3  <=  num1  e  num3  <=  num2  e  num1  <=  num2 :
    print ( f"A ordem crescente é { num3 } , { num1 } e { num2 } " )
elif  num3  <=  num1  e  num3  <=  num2  e  num2  <=  num1 :
    print ( f"A ordem crescente é { num3 } , { num2 } e { num1 } " )
