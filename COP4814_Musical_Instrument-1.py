"""This serves as a template for Lab #1 - Strategy for Musical Instruments"""

# Don't forget to implement ABC and use @abstractmethod decorator when appropriate
###############################################################################
# Instruments
###############################################################################
from abc import ABC, abstractmethod

"""The Instrument interface contains one class variable named play_behavior 
and three methods: display, play and set_play_behavior"""
class Instrument(ABC):

    play_behavior = None

    #Abstract method to display the instrument
    @abstractmethod
    def display(self):
        pass

    #Method to perform the play action using the play behavior
    def perform_play(self):
        self.play_behavior.play()

    #Method to set a new play behavior
    def set_play_behavior(self, newplay_behavior):
        self.play_behavior = newplay_behavior

"""The DoubleBass class is already written for you! :)
You should use as a template for the following 4 classes"""

class DoubleBass(Instrument):
    #Setting the play behavior for DoubleBass
    def __init__(self):
        self.play_behavior = PlayWithBow()

    #Displays method to show that it is a double bass
    def display(self):
        print("I am a double bass.")


class Clarinet(Instrument):
    #Setting the play behavior for the Clarinet
    def __init__(self):
        self.play_behavior = BuzzAReed()

    #Display method will show that it is a clarinet
    def display(self):
        print("I am a clarinet.")


class Harp(Instrument):
    #Setting the play behavior for the Harp
    def __init__(self):
        self.play_behavior = PluckWithFingers()

    #Display method to show that it is a harp
    def display(self):
        print("I am a harp.")


class Tuba(Instrument):
    #Setting the play behavior for the Tuba
    def __init__(self):
        self.play_behavior = BuzzWithLips()

    #Display method to show tht it is a tuba
    def display(self):
            print("I am a tuba.")


class Violin(Instrument):
    #Setting the play behavior for the Violin
    def __init__(self):
        self.play_behavior = PlayWithBow()


    #Display method to show that it is a violin
    def display(self):
            print("I am a violin.")

###############################################################################
# Play behaviors
###############################################################################

"""The PlayBehavior interface is already implemented"""
class PlayBehavior:

    @abstractmethod
    def play(self):
        pass

class PlayWithBow(PlayBehavior):

    #Play method to show the action of playing with bow
    def play(self):
        print("Play me with a bow.")


class BuzzAReed(PlayBehavior):

    # Play method to show the action of buzzing a reed
    def play(self):
        print("Play me by blowing and buzzing a reed.")


class BuzzWithLips(PlayBehavior):

    # Play method to show the action of buzzing with lips
    def play(self):
        print("Play me by blowing and buzzing with your lips.")


class PluckWithFingers(PlayBehavior):

    # Play method to show the action of plucking with fingers
    def play(self):
        print("Play me by plucking my strings.")


"""I already instantiated some objects and created a list containing those objects
in the for loop the methods display and play are called for each object. Then a new
object of DoubleBass() is instantiated, but a setter methods was called to change the
behavior of this object"""

#Main execution block
if __name__ == '__main__':
    #Instatiate the Instruments
    violin = Violin()
    tuba = Tuba()
    clarinet = Clarinet()
    harp = Harp()
    doublebass = DoubleBass()

    #Lis of all instrument objects
    instruments = [violin,tuba,clarinet,harp,doublebass]

    #for loop to iterate over each instrument from the list
    for i in instruments:
        i.display()         #Calls display method to show the instrument type
        i.perform_play()    #Call the perform_play method to demonstrate the playbehaviors

    new_doublebass = DoubleBass()                         #Create a new DoubleBass object
    new_doublebass.set_play_behavior(PluckWithFingers())  #Change the play behavior of the new DoubleBass object
    new_doublebass.perform_play()                         #Double pass will perform pluck behavior
