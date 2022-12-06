import unittest
from montecarlo import *
class TestCase(unittest.TestCase):
    
    def test_die_length(self):
        Test_Die = Die([1,2,3,4])
        Expected_Length = 4
        # Number of rows is the same as it should be
        self.assertEqual(len(Test_Die.die), Expected_Length)
        
    def test_change_weight(self):
        Test_Die = Die([1,2,3,4])
        Test_Die.change_weight(2,2)
        # Test if the weight was changed
        self.assertEqual(Test_Die.die[Test_Die.die['faces'] == 2]['weights'].reset_index(drop = True).pop(0), 2)
    
    def test_roll_length(self):
        Test_Die = Die([1,2,3,4])
        roll = Test_Die.roll(3)
        # Test to see if the three rolls were produced
        self.assertEqual(len(roll), 3)
        
    def test_show_dataframe(self):
        Test_Die = Die([1,2,3,4])
        # Test to see if a dataframe is returned
        self.assertEqual(type(Test_Die.show()), type(pd.DataFrame()))
    
    def test_die_set_length(self):
        Test_Die = Die([1,2,3,4])
        Test_Game = Game([Test_Die, Test_Die, Test_Die])
        # Test to see if there are 3 die in the set
        self.assertEqual(len(Test_Game.die_set), 3)
    
    def test_game_play_length(self):
        Test_Die = Die([1,2,3,4])
        Test_Game = Game([Test_Die, Test_Die, Test_Die])
        Test_Game.play(10)
        # Test to see if there are 10 rolls
        self.assertEqual(len(Test_Game.result_df), 10)
    
    def test_game_show_dataframe(self):
        Test_Die = Die([1,2,3,4])
        Test_Game = Game([Test_Die, Test_Die, Test_Die])
        Test_Game.play(10)
        # Test to see if show returns a dataframe
        self.assertEqual(type(Test_Game.show()), type(pd.DataFrame()))
        
    def test_face_counts_per_roll_length(self):
        Test_Die = Die([1,2,3,4])
        Test_Game = Game([Test_Die, Test_Die, Test_Die])
        Test_Game.play(10)
        Test_Analyzer = Analyzer(Test_Game)
        Test_Analyzer.face_counts_per_roll()
        # Test to see if there are the right number of faces
        self.assertEqual(len(Test_Analyzer.face_counts.axes[1]), 4)
        
    def test_jackpot_type(self):
        Test_Die = Die([1,2,3,4])
        Test_Game = Game([Test_Die, Test_Die, Test_Die])
        Test_Game.play(10)
        Test_Analyzer = Analyzer(Test_Game)
        # Test to see if jackpot returns an integer
        self.assertEqual(type(Test_Analyzer.jackpot()), int)
        
    def test_combo_method(self):
        Test_Die = Die([1,2,3,4])
        Test_Game = Game([Test_Die, Test_Die, Test_Die])
        Test_Game.play(10)
        Test_Analyzer = Analyzer(Test_Game)
        Test_Analyzer.combo()
        # Test to see if the index is a MultiIndex
        self.assertEqual(type(Test_Analyzer.combo.index), pd.core.indexes.multi.MultiIndex)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)