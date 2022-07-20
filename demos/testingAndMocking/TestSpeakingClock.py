import unittest.mock
import datetime
from unittest.mock import MagicMock
from unittest.mock import patch
from clock.Clock import Clock
from clock.SpeakingClock import SpeakingClock


class TestSpeakingClock(unittest.TestCase):

    def test_speaking_clock_gets_time_from_clock(self):
        # arrange
        #  create the clock
        mock_clock = Clock()
        # mock the get_time method to always return midday
        mock_clock.get_time = MagicMock(return_value = datetime.datetime(2017,12,1,12,0,0))
        # create the speaking clock and then assign the mock_clock to be used instead of a normal clock
        speaking_clock = SpeakingClock()
        speaking_clock.clock = mock_clock
        # act
        # invoke the say_time method
        return_value = speaking_clock.say_time()
        # assert
        # check that the clock was asked what the time is
        # mock is acting as a spy
        mock_clock.get_time.assert_called_once()
        # check that the value returned from the speaking clock is actually 'midday' given that is the time
        self.assertEqual(return_value, 'midday')



    # This only works with Python 3.6.x. It does not work with Python 3.5.x
    def test_speaking_clock_gets_time_from_clock_with_patching(self):
        with patch.object(Clock, 'get_time', return_value=datetime.datetime(2017,12,1,12,0,0)) as mock_method:
            speaking_clock = SpeakingClock()
            return_value = speaking_clock.say_time()
            mock_method.assert_called_once()
            self.assertEqual(return_value, 'midday')



if __name__ == '__main__':
    unittest.main()