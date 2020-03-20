
# You have been given a robot with very basic capabilities:

# It can move left or right.
# It can pick up an item
# If it tries to pick up an item while already holding one, it will swap the items instead.
# It can compare the item it's holding to the item in front of it.
# It can switch a light on its head on or off.
# Your task is to program this robot to sort lists using ONLY these abilities.

# We discussed a sorting method this week that might be useful. Which one? Selection sort

# The robot has exactly one bit of memory: its light. Why is this important?
# It allows you to use it as a trigger


class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    #plan
    #if the light is on it will start storting 
    # use a while loop because it is sorting so while true
    # start with the first item in the list and pick it up
    # move right and compare it with the second item
    # if item is smaller go to next one
    #if it is bigger swap it
    # go through the whole list to find the biggest one and then sort it to the end

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
         
         
        # to start the loop like a on switch
        self.set_light_on()
        # set it back to off so we can use it again later
        while(self.light_is_on()):
            self.set_light_off() 
             # picking up the first item because the robot is holding none, but it will put none in the list. need to pick it back up
            while(self.can_move_right()):
                self.swap_item()
                # move right once
                self.move_right() 
                 #checking the size of the number to check if it is bigger
                if(self.compare_item() == 1):
                    self.swap_item()
                    

                    #got to pick none back up               
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    # found a swap and should continue sorting
                    self.set_light_on() 
                # did not find a swap so go back and pick up none again
                   
                else: 
                    self.move_left()
                    self.swap_item()
                    self.move_right()
            #go back to the start
            while(self.can_move_left()):
                self.move_left()






if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 1, 332, 49, 2]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)