# Luyu Wu Vankerkwijk - ESC180 Project #1 - September 27th 2025

def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars
    
    cur_hedons = 0
    cur_health = 0
    
    cur_star = None
    cur_star_activity = None
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    last_finished = -1000
    

            

def star_can_be_taken(activity):
    return activity == cur_star and not bored_with_stars

    
def perform_activity(activity, duration):
    global last_activity, last_activity_duration, cur_time
    global cur_health, cur_hedons
    global cur_star, cur_star_activity
    
    tired = last_finished < 120

    if activity == "running":
        last_dur = 0
        if last_activity == "running":
            last_dur = last_activity_duration
        for i in range(duration):
            last_dur += 1
            cur_time += 1
            if last_dur <= 180:
                cur_health += 3
            else:
                cur_health += 1
            if tired:
                cur_hedons -= 2
            else:
                if i < 10:
                    cur_hedons += 2
                else:
                    cur_hedons -= 2
            if cur_star_activity == activity and i<10:
                  cur_hedons += 3  
    elif activity == "textbooks":
        for i in range(duration):
            cur_time += 1
            cur_health += 2
            if tired:
                cur_hedons -= 2
            else:
                if i < 20:
                    cur_hedons += 1
                else:
                    cur_hedons -= 1
            if cur_star_activity == activity and i<10:
                cur_hedons += 3
    elif activity == "resting":
        cur_time += duration

    last_activity = activity
    last_activity_duration = duration
    cur_star = None
    cur_star_activity = None
    
def get_cur_hedons():
    return cur_hedons
    
def get_cur_health():
    return cur_health
    
def offer_star(activity):
    global cur_star
    cur_star = activity
        
def most_fun_activity_minute():
    tired = last_finished < 120
    if cur_star_activity:
        return cur_star_activity
    if tired:
        return "resting"
    elif last_activity_duration > 180 and last_activity == "running":
        return "textbooks"
    else:
        return "running"
    
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    
def get_effective_minutes_left_health(activity):
    pass    

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass
            

def estimate_health_delta(activity, duration):
    pass
        
################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
