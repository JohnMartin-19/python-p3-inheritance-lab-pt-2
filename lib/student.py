class Student:
    def __init__(self,name):
        self.name = name
    
    def hello(name):
        print(f'{name},hello there!Im so excited to learn stuff')

    def raise_hand():
        print('pick me bro!')
    

class ChattyStudent(Student):
    def __init__(self,hello):
        super().__init__(hello)
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self,raise_hand):
        super().__init__(raise_hand)
        print(('pick me!')* 10)


    

