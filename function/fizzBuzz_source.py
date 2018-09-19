import json
def fizzBuzz(request):
    
    returnJson = {}
    returnJson['status'] = {}    
	
    # check if max_range is an available parameter
    if request.args and 'max_range' in request.args:
        maxRange = request.args.get('max_range')
        
        # verify max_range is a valid int
        try:
            int(maxRange)
        except ValueError:
            returnJson['status']['code'] = 400
            returnJson['status']['message'] = 'Error: max_range must be an integer'
            return json.dumps(returnJson)
        
    # otherwise default to 100
    else:
        maxRange = 100
        
    returnJson['status']['code'] = 200
    returnJson['status']['message'] = 'Success' 
    
    output = ''
   
    for val in range(0, int(maxRange)+1):
        temp = ''
        
        if val % 3 == 0 and val % 5 == 0:
            temp = 'FizzBuzz'
        elif val % 3 == 0:
            temp = 'Fizz'
        elif val % 5 == 0:
            temp = 'Buzz'
        else:
            temp = str(val)            
        output += temp + ', '
      
    #remove trailing ', ' chars
    output = output[:-2]
   
    returnJson['data'] = output
    
    return json.dumps(returnJson)
