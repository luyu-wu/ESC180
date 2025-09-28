# Luyu Wu Vankerkwijk - ESC180 Project #1 - September 27th 2025

def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars
    global star_times
    global cur_star
    
    cur_hedons = 0
    cur_health = 0
    
    cur_star = None
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    last_finished = -1000
    star_times = []
    

def star_can_be_taken(activity):
    # Do not need to define other conditions, as they are taken care of
    # E.g. perform activity automatically removes current stars once finished
    # E.g. setting stars checks if user is tired of stars before setting
    return (activity == cur_star)

def perform_activity(activity, duration):
    global last_activity, last_activity_duration, cur_time, last_finished
    global cur_health, cur_hedons
    global cur_star
    
    tired = (cur_time-last_finished) < 120

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

            if cur_star == activity and i<10:
                  cur_hedons += 3
        last_finished = cur_time
        duration = last_dur
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
            if cur_star == activity and i<10:
                cur_hedons += 3
        last_finished = cur_time
    elif activity == "resting":
        cur_time += duration

    last_activity = activity
    last_activity_duration = duration
    cur_star = None
    
def get_cur_hedons():
    return cur_hedons
    
def get_cur_health():
    return cur_health
    
def offer_star(activity):
    global cur_star, star_times, bored_with_stars
    star_times.append(cur_time)
    if len(star_times) > 2:
        bored_with_stars =  (cur_time - star_times[-3]) < 120
    if not bored_with_stars:
        cur_star = activity
        
def most_fun_activity_minute():
    tired = cur_time-last_finished < 120
    if cur_star:
        return cur_star
    if tired:
        return "resting"
    elif last_activity_duration > 180 and last_activity == "running":
        return "textbooks"
    else:
        return "running"
