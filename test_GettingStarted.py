#Testin with pytest
import baseClass as bc


class TestClass:
    def test_warren(self):
        me = bc.baseClass()
        assert 0 == me.beer

    def test_givebeer(self):
        me = bc.baseClass()
        me.giveBeer()
        assert 1 == me.beer

    def test_initial(self):
        me = bc.baseClass()
        assert False == me.isHappy()

    def test_method(self):
        me = bc.baseClass()
        me.giveBeer()
        assert True == me.isHappy()

    def test_id(self):
        me = bc.baseClass()
        assert 1 == me.id

