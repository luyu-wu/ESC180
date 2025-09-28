import gamify

def test_tired_running_star_hedons_points_when_running_1min():
    """Test hedons with running star when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)  # Get tired
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons-2+3  # Tired penalty + star bonus

def test_tired_running_star_hedons_points_when_running_11min():
    """Test hedons with running star for 11min when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)  # Get tired
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('running', 11)
    assert gamify.get_cur_hedons() == start_hedons-2*11+30  # Tired penalty + star bonus

def test_tired_carrying_star_hedons_points_when_carrying_1min():
    """Test hedons with textbooks star when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)  # Get tired
    gamify.offer_star("textbooks")
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons-2+3  # Tired penalty + star bonus

def test_tired_star_hedons_points_rest_run():
    """Test hedons after rest then run with star"""
    gamify.initialize()
    gamify.perform_activity("running", 1)  # Get tired
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_star_most_fun_act():
    """Test most fun activity with star when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)  # Get tired
    gamify.offer_star('running')
    assert gamify.most_fun_activity_minute() == 'running'

def test_tired_star_three_starts_in_2hrs_1():
    """Test complex star sequence - scenario 1"""
    gamify.initialize()
    gamify.perform_activity("running", 1)  # Get tired
    gamify.offer_star('running')
    start_health = 3
    start_hedons = 2

    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2+3

    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_hedons() == start_hedons-2

if __name__ == '__main__':
    # Run all tired with star tests
    test_tired_running_star_hedons_points_when_running_1min()
    test_tired_running_star_hedons_points_when_running_11min()
    test_tired_carrying_star_hedons_points_when_carrying_1min()
    test_tired_star_hedons_points_rest_run()
    test_tired_star_most_fun_act()
    test_tired_star_three_starts_in_2hrs_1()
    test_tired_star_three_starts_in_2hrs_4()
    print("All tired with star tests passed!")
