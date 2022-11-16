



class test_should_tweak_name:
    

    def __init__(self, name) -> None:
        self.name = name
        
    
    def test_should_addNames(self, name):
        new_name = self.name+" "+name

        assert new_name == "Idowu Omisola", "new_name should be Idowu Omisola"

        return new_name

    def test_should_changeName(self, name):
        new_name = name
        assert new_name == "Paul", "new_name should be Paul" 
        return name