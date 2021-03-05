# Flask API

Its a simple API which returns Sum , Sub , Product of two numbers  also the factorial of a number given as an input via url.

For example - 

1] If we Run this on IP - > http://127.0.0.1:5000/math/5/2

     It returns a JSON as follows:
       
             {
               "Product is ": 10, 
               "Sub is ": 3, 
               "Sum is ": 7
             }
             
             
2] For - >  http://127.0.0.1:5000/fact/5  
    
    It returns a JSON as follows:
            
            {
               "Factorial is": 120
            }
