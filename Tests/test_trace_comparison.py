import random
import json
import unittest

from Managers.GameDirector import GameDirector
from Agents.RandomAgent import RandomAgent as ra
from Agents.AdrianHerasAgent import AdrianHerasAgent as aha

class TestTraces(unittest.TestCase):
    
    def test_fast_ra_ra_aha_aha(self):
        game_director = GameDirector(agents=(ra, ra, aha, aha), max_rounds=200, output_traces=False)
        for i in range(10):
            random.seed(i)
            game_trace = game_director.game_start(i, False)
            game_hash = hash(json.dumps(game_trace)) # convert to string because dict is not hashable
            with open(f'./Tests/test_traces/game_{i}.json', 'r') as f:
                test_hash = hash(f.read())

            self.assertEqual(game_hash, test_hash)
    

    def test_ra_ra_aha_aha(self):
        game_director = GameDirector(agents=(ra, ra, aha, aha), max_rounds=200, output_traces=False)
        for i in range(100):
            random.seed(i)
            game_trace = game_director.game_start(i, False)
            game_hash = hash(json.dumps(game_trace)) # convert to string because dict is not hashable
            with open(f'./Tests/test_traces/game_{i}.json', 'r') as f:
                test_hash = hash(f.read())

            self.assertEqual(game_hash, test_hash)

if __name__ == '__main__':
    unittest.main()