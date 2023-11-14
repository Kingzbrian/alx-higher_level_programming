"""
unittests for rectangle class
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    rectangle test class
    """
    def setUp(self) -> None:
        self.instance = Rectangle(4, 6, 2, 0)

    def test_rectangle_init(self):
        """
        Tests for rectangle initializations
        """
        rectangle1 = Rectangle(2, 5)
        self.assertEqual(rectangle1.id, 4)
        self.assertEqual(rectangle1.id, Rectangle._Base__nb_objects)
        rectangle1 = Rectangle(2, 5)
        self.assertEqual(rectangle1.width, 2)
        self.assertEqual(rectangle1.height, 5)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.y, 0)
        self.assertEqual(rectangle1.id, 5)
        rectangle3 = Rectangle(3, 6, 2, 5)
        self.assertEqual(rectangle3.width, 3)
        self.assertEqual(rectangle3.height, 6)
        self.assertEqual(rectangle3.x, 2)
        self.assertEqual(rectangle3.y, 5)
        self.assertEqual(rectangle3.id, 6)

    def test_str(self):
        """
        tests for the rectangle str method
        """
        r1 = self.instance
        expected = "[Rectangle] (7) 2/0 - 4/6"
        self.assertEqual(str(r1), expected)

    def test_validator_width(self):
        """
        tests for the validator method
        """
        self.assertIsNone(self.instance.validator("width", 5))

    def test_validator_height(self):
        """
        tests for the validator method
        """
        self.assertIsNone(self.instance.validator("height", 7))

    def test_validator_x(self):
        """
        tests for the validator method
        """
        self.assertIsNone(self.instance.validator("x", 0, True))

    def test_validator_y(self):
        """
        tests for the validator method
        """
        self.assertIsNone(self.instance.validator("y", 0, True))

    def test_validator_height_0_or_less(self):
        with self.assertRaises(ValueError) as error:
            self.instance.validator("height", -5)
        self.assertEqual(str(error.exception), "height must be > 0")

    def test_validator_width_not_int(self):
        with self.assertRaises(TypeError) as error:
            self.instance.validator("width", "10")
        self.assertEqual(str(error.exception), "width must be an integer")

    def test_validator_x_less_than_0(self):
        with self.assertRaises(ValueError) as error:
            self.instance.validator("x", -10, True)
        self.assertEqual(str(error.exception), "x must be >= 0")

    def test_validator_y_not_int(self):
        with self.assertRaises(TypeError) as error:
            self.instance.validator("y", "10", True)
        self.assertEqual(str(error.exception), "y must be an integer")

    def test_area(self):
        r1 = self.instance
        self.assertEqual(Rectangle.area(r1), 24)

    def test_display(self):
        r1 = self.instance
        expected = "  ####\n  ####\n  ####\n  ####\n  ####\n  ####\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Rectangle.display(r1)
            output = mock_stdout.getvalue()
        self.assertEqual(output, expected)

    def test_update_args(self):
        self.instance.update(10, 2, 3, 1, 1)
        self.assertEqual(self.instance.id, 10)
        self.assertEqual(self.instance.width, 2)
        self.assertEqual(self.instance.height, 3)
        self.assertEqual(self.instance.x, 1)
        self.assertEqual(self.instance.y, 1)

    def test_update_kwargs(self):
        self.instance.update(id=9, width=3, height=4, x=2, y=2)
        self.assertEqual(self.instance.id, 9)
        self.assertEqual(self.instance.width, 3)
        self.assertEqual(self.instance.height, 4)
        self.assertEqual(self.instance.x, 2)
        self.assertEqual(self.instance.y, 2)

    def test_to_dictionary(self):
        r1 = self.instance
        result = {'x': 2, 'y': 0, 'id': 8, 'height': 6, 'width': 4}
        self.assertEqual(Rectangle.to_dictionary(r1), result)


if __name__ == "__main__":
    unittest.main()
