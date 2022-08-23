# Complete the function definition to return the hours given minutes. 

# Sample output with input: 210.0
# 3.5

def get_minutes_as_hours(orig_minutes):

    result= orig_minutes/60
    return(result)

minutes = float(input())
print(get_minutes_as_hours(minutes))
