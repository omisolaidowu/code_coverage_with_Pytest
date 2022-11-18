



class test_should_tweak_name:
    

    def __init__(self, name) -> None:
        self.name = name
        
    
    def test_should_addNames(self, name):
        new_name = self.name+" "+name

        assert new_name == "LambdaTest Grid", "new_name should be LambdaTest Grid"

        return new_name

    def test_should_changeName(self, name):
        self.name = name
        assert self.name == "LambdaTest Cloud Grid", "new_name should be LambdaTest Cloud Grid" 
        return name