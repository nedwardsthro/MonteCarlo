import numpy as np
import pandas as pd

class Die:
    '''
    Purpose: Create a die to be rolled with different weights
    Inputs:
        - faces : List of faces for the die
    '''
    def __init__(self, faces):
        self.die = pd.DataFrame({
            'faces': faces,
            'weights': np.ones(len(faces))
        })
    
    def change_weight(self, face_value, new_weight):
        '''
        Purpose: Change the weight of a single face on the die
        Inputs:
            - faces : face name to be changed
            - new_weight: new weight of the face
        '''
        self.die.loc[self.die.faces == face_value, 'weights'] = new_weight
        
    def roll(self, nrolls = 1):
        '''
        Purpose: Roll a die based on the current weights of the die
        Inputs:
            - nrolls : number of rolls
        Outputs:
            - Result of the rolls
        '''
        self.my_probs = [i/sum(self.die.weights) for i in self.die.weights]
        results = []
        for i in range(nrolls):
            result = self.die.sample(weights=self.die.weights).values[0][0]
            results.append(result)
        return(results)
        
    def show(self):
        '''
        Purpose: Show the current die faces and weights
        Outputs:
            - Dataframe of the die faces and weights
        '''
        return(self.die)
        
class Game:
    '''
    Purpose: To roll a set of dice a certain number of times and store the result
    Inputs:
        - die_set: List of die objects
    '''
    def __init__(self, die_set):
        self.die_set = die_set
    
    def play(self, nrolls):
        '''
        Purpose: Roll the die set nrolls times and store the combinations
        Inputs:
            - nrolls: Number of times to roll each dice in the set
        '''
        self.result_df = pd.DataFrame()
        for i in range(0, len(self.die_set)):
            die = self.die_set[i]
            self.result_df[i] = die.roll(nrolls)
        self.result_df = self.result_df.rename_axis(columns = "Faces")
        self.result_df.index.rename('Roll_Number', inplace = True)
        
    def show(self, df_format = 'wide'):
        '''
        Purpose: Show the rolls of the die set in either a narrow or wide format
        Inputs:
            - df_format: "narrow" or "wide", how you want to df to be returned 
        Outputs:
            - Dataframe with the results of the game
        '''
        if df_format == "wide":
            return(self.result_df)
        elif df_format == "narrow": 
            df = self.result_df.stack().to_frame().reset_index().rename(columns = {'Roll_Number':'Roll_Number', 'Faces':'Die_Number', 0:'Face'}).set_index(['Roll_Number', 'Die_Number'])
            return(df)
        else:
            print("df_format must be 'narrow' or 'wide'")

class Analyzer:
    '''
    Purpose: Analyze a game class and find different combinations and face counts
    Inputs:
        - Game: a game class
    '''
    def __init__(self, Game):
        self.Game = Game
    
    def face_counts_per_roll(self):
        '''
        Purpose: Find the number of times each face appears in each roll
        '''
        self.face_counts = self.Game.show("wide").copy().apply(pd.Series.value_counts, axis=1).fillna(0).rename_axis(columns = "Faces")
    
    def combo(self):
        '''
        Purpose: Find the different combinations of faces that appear in each roll and count the number of times they appear
        '''
        df = self.Game.show("wide").copy()
        df['list'] = pd.Series(df.astype(str).values.tolist()).apply(lambda x: sorted(x))
        inter = df.sort_values("list")['list'].value_counts().to_frame().reset_index().sort_values('index').reset_index(drop = True)
        self.combo = pd.DataFrame(inter['index'].tolist()).reset_index(drop = True)
        self.combo['Count'] = inter['list']
        self.combo = self.combo.set_index(self.combo.columns.difference(['Count'], sort = False).tolist())
    
    def jackpot(self):
        '''
        Purpose: Count the number of times a roll returns all of the same faces
        Output:
            - An integer of the number of times all of the faces were the same
        '''
        self.jackpot = self.Game.show("wide").copy()
        self.jackpot['list'] = pd.Series(self.jackpot.astype(str).values.tolist()).apply(lambda x: sorted(x))
        self.jackpot['uniques'] = self.jackpot['list'].explode().groupby('Roll_Number').unique()
        self.jackpot['Jackpot'] = np.where(self.jackpot['uniques'].str.len() == 1, True, False)
        self.jackpot = self.jackpot[self.jackpot['Jackpot'] == True]
        total_jackpots = sum(self.jackpot['Jackpot'])
        return(total_jackpots)