import click
import unittest
import apeiron

from click.testing import CliRunner

class TestSum(unittest.TestCase):

    def test_apeiron_help(self):
        runner = CliRunner()
        result = runner.invoke(apeiron.cli, ['--help'])
        self.assertEqual(result.exit_code,0,'Should be 0')

if __name__ == '__main__':
    unittest.main()