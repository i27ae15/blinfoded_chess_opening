from unittest import TestCase

import tensorflow as tf

from core.testing import print_starting, print_success
from core.printing import __print__ as print

from alpha_zero.alpha_zero import AlphaZero
from alpha_zero.neural_network import create_chess_cnn


class AlphaZeroTest(TestCase):

    def test_self_play(self):

        print_starting()

        alpha_zero = AlphaZero(
            depth_of_search=15,
        )

        # test self play

        model = create_chess_cnn((8, 8, 12), 546)

        alpha_zero.self_play(
            model=model,
            num_games=1,
            num_iterations=1,
            model_save_path='model_v0_1.keras'
        )

        print_success()

    def t_self_play_with_loaded_model(self):

        print_starting()

        alpha_zero = AlphaZero(
            depth_of_search=15,
        )

        model = tf.keras.models.load_model('model_v0_1.keras')

        alpha_zero.self_play(
            model=model,
            num_games=1,
            num_iterations=20,
            model_save_path='model_v0_1.keras'
        )

        print_success()
