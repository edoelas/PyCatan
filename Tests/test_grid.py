import unittest
from Classes.Grid import Tile
from Classes.Grid import Edge
from Classes.Grid import Vertex

class TestTile(unittest.TestCase):

    def test_get_all_adjacent(self):

        self.assertEqual(
            Tile.get_all_adjacent({Tile(-1,1)}),
            {Tile(0,1), Tile(0,0),Tile(-2,1), Tile(-1,0),Tile(-2,2), Tile(-1,2)}
        )

        self.assertEqual(
            Tile.get_all_adjacent({Tile(0, 0), Tile(1, 0)}),
            {Tile(0,1), Tile(1,-1)}
        )

        self.assertEqual(
            Tile.get_all_adjacent({Tile(0, 0), Tile(1, 0), Tile(0, 1)}),
            set()
        )

        
    def test_are_all_adjacent(self):

        self.assertFalse(
            Tile.are_all_adjacent({Tile(-1,1), Tile(0,1), Tile(0,0),Tile(-2,1), Tile(-1,0),Tile(-2,2), Tile(-1,2)})
        )

        self.assertTrue(
            Tile.are_all_adjacent({Tile(0, 0), Tile(1, 0)})
        )

        self.assertTrue(
            Tile.are_all_adjacent({Tile(0, 0), Tile(1, 0), Tile(0, 1)})
        )

        self.assertRaises(
            ValueError,
            Tile.are_all_adjacent,
            {Tile(0, 0)}
        )

    def test_eq(self):

        self.assertTrue(
            Tile(0, 0) == Tile(0, 0)
        )

        self.assertFalse(
            Tile(0, 0) == Tile(1, 0)
        )

    def test_sub(self):
            
            self.assertEqual(
                Tile(0, 0) - Tile(1, 0),
                Tile(-1, 0)
            )
    
            self.assertEqual(
                Tile(1, 0) - Tile(0, 0),
                Tile(1, 0)
            )

            self.assertEqual
            (
                Tile(0, 0) - Tile(0, -1),
                Tile(0, 1)
            )

    def test_add(self):
            
            self.assertEqual(
                Tile(0, 0) + Tile(1, 0),
                Tile(1, 0)
            )
    
            self.assertEqual(
                Tile(1, 0) + Tile(0, 0),
                Tile(1, 0)
            )

            self.assertEqual
            (
                Tile(0, 0) + Tile(0, -1),
                Tile(0, -1)
            )

    def test_adjacent_tiles(self):

        self.assertEqual(
            Tile(0, 0).adjacent_tiles(),
            {Tile(1, 0), Tile(0, 1), Tile(-1, 1), Tile(-1, 0), Tile(0, -1), Tile(1, -1)}
        )

        self.assertEqual(
            Tile(1, 0).adjacent_tiles(),
            {Tile(2, 0), Tile(1, 1), Tile(0, 1), Tile(0, 0), Tile(1, -1), Tile(2, -1)}
        )

        self.assertEqual(
            Tile(-2,1).adjacent_tiles(),
            {Tile(-1, 1), Tile(-2, 2), Tile(-3, 2), Tile(-3, 1), Tile(-2, 0), Tile(-1, 0)}
        )

    def test_adjacent_edges(self):
            
            self.assertEqual(
                Tile(0, 0).adjacent_edges(),
                {Edge({Tile(0, 0), Tile(1, 0)}), Edge({Tile(0, 0), Tile(0, 1)}), Edge({Tile(-1, 0), Tile(0, 0)}),
                Edge({Tile(0, 0), Tile(-1, 1)}), Edge({Tile(0, 0), Tile(0, -1)}), Edge({Tile(0, 0), Tile(1, -1)})}
            )
    
            self.assertEqual(
                Tile(1, 0).adjacent_edges(),
                {Edge({Tile(1, 0), Tile(2, 0)}), Edge({Tile(1, 0), Tile(1, 1)}), Edge({Tile(0, 1), Tile(1, 0)}),
                Edge({Tile(1, 0), Tile(0, 0)}), Edge({Tile(1, 0), Tile(1, -1)}), Edge({Tile(1, 0), Tile(2, -1)})}
            )
    
            self.assertEqual(
                Tile(-2,1).adjacent_edges(),
                {Edge({Tile(-2, 1), Tile(-1, 1)}), Edge({Tile(-2, 1), Tile(-2, 2)}), Edge({Tile(-3, 2), Tile(-2, 1)}),
                Edge({Tile(-2, 1), Tile(-3, 1)}), Edge({Tile(-2, 1), Tile(-2, 0)}), Edge({Tile(-2, 1), Tile(-1, 0)})}
            )

    def test_adjacent_vertexes(self):

        self.assertEqual(
            Tile(0, 0).adjacent_vertexes(),
            {Vertex({Tile(0, -1), Tile(1, -1), Tile(0, 0)}), Vertex({Tile(-1, 0), Tile(0, -1), Tile(0, 0)}),
            Vertex({Tile(1, 0), Tile(1, -1), Tile(0, 0)}), Vertex({Tile(-1, 0), Tile(-1, 1), Tile(0, 0)}),
            Vertex({Tile(0, 1), Tile(-1, 1), Tile(0, 0)}), Vertex({Tile(0, 1), Tile(1, 0), Tile(0, 0)})}
        )

if __name__ == '__main__':
    unittest.main()