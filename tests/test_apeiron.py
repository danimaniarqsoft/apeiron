import click
import unittest
import apeiron

from click.testing import CliRunner

# Initialization
runner = CliRunner()

class TestApeironCommand(unittest.TestCase):

    def test_apeiron_help(self): 
        result = runner.invoke(apeiron.cli, ['--help'])
        self.assertEqual(result.exit_code,0,'Should be 0')

if __name__ == '__main__':
    unittest.main()