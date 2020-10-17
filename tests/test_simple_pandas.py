import unittest
import pandas as pd
from pandas._testing import assert_frame_equal
from simple.simple import simple_pandas


class TestSimplePandas(unittest.TestCase):
    def test_simple_pandas(self):
        dummy = pd.DataFrame(
            data={'col1': [1, 2], 'col2': [3, 4]}
        )
        out = simple_pandas()
        assert_frame_equal(
            out,
            dummy
        )


if __name__ == '__main__':
    unittest.main()
