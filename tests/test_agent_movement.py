import pytest

import pandas as pd

from agents import behaviour

@pytest.fixture
def small_df():
    data = {'x': 0, 'y': 0, 'vx': 1, 'vy': 5}
    df = pd.DataFrame(data)
    return df

def test_behaviour_move_agent(small_df: pd.DataFrame):
    df_move = behaviour.move_agent(small_df, dt=1.)
    x_test = df_move['x'] == pytest.approx(1, rel=0.99)
    y_test = df_move['y'] == pytest.approx(5, rel=0.99)
    assert x_test and y_test
