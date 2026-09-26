import logging
import os
import tempfile
import unittest
from unittest.mock import patch
from src.employee_management import logging_config

class TestLoggingConfig(unittest.TestCase):
    @patch("src.employee_management.logging_config.logging.basicConfig")
    def test_setup_logging(self, mock_basic_config):
        with tempfile.TemporaryDirectory() as temp_dir:
            log_folder = os.path.join(temp_dir, "logs")
            log_file = os.path.join(log_folder, "application.log")
            with patch.object(logging_config, "LOG_FOLDER", log_folder):
                with patch.object(logging_config, "LOG_FILE", log_file):
                    logging_config.setup_logging()

            self.assertTrue(os.path.exists(log_folder))
            mock_basic_config.assert_called_once_with(filename=log_file,level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    unittest.main()