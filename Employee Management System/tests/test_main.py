import json
import unittest
from unittest.mock import mock_open, patch
from src import main

class TestLoadData(unittest.TestCase):
    def setUp(self):
        main.employees.clear()

    def tearDown(self):
        main.employees.clear()

    @patch("src.main.os.path.exists", return_value=False)
    def test_load_data_when_file_does_not_exist(self, mock_exists):
        main.load_data()
        self.assertEqual(main.employees, [])
    @patch("src.main.os.path.exists", return_value=True)
    @patch("builtins.open",mock_open(read_data=json.dumps([{"id": 101,"name": "Rahul"}])))

    def test_load_valid_employee_data(self, mock_exists):
        main.load_data()
        self.assertEqual(len(main.employees), 1)
        self.assertEqual(main.employees[0]["id"], 101)
        self.assertEqual(main.employees[0]["name"], "Rahul")
    @patch("src.main.os.path.exists", return_value=True)
    @patch("builtins.open",mock_open(read_data='{"id": 101}'))

    def test_load_data_when_json_is_not_a_list(self, mock_exists):
        main.load_data()
        self.assertEqual(main.employees, [])
    @patch("src.main.os.path.exists", return_value=True)
    @patch("builtins.open",mock_open(read_data=json.dumps([{"id": 0,"name": "Invalid Employee"}])))

    def test_load_data_with_invalid_employee(self, mock_exists):
        main.load_data()
        self.assertEqual(main.employees, [])
    @patch("src.main.os.path.exists", return_value=True)
    @patch("builtins.open",mock_open(read_data="{invalid json"))

    def test_load_data_with_invalid_json(self, mock_exists):
        main.load_data()
        self.assertEqual(main.employees, [])
    @patch("src.main.os.path.exists", return_value=True)
    @patch("builtins.open",side_effect=OSError("File could not be opened"))

    def test_load_data_when_file_cannot_be_read(self,mock_open_file,mock_exists):
        main.load_data()
        self.assertEqual(main.employees, [])
        mock_open_file.assert_called_once_with(main.DATA_FILE,"r")

class TestSaveData(unittest.TestCase):
    def setUp(self):
        main.employees.clear()
        
    def tearDown(self):
        main.employees.clear()

    @patch("src.main.open", new_callable=mock_open)
    def test_save_employee_data(self, mock_file):
        main.employees.append({"id": 101,"name": "Rahul"})
        main.save_data()
        mock_file.assert_called_once_with(main.DATA_FILE,"w")
        file_handle = mock_file()
        file_handle.write.assert_called()
        written_data = ""
        for call in file_handle.write.call_args_list:
            written_data += call.args[0]
        saved_data = json.loads(written_data)
        self.assertEqual(saved_data,[{"id": 101,"name": "Rahul"}])

    @patch("src.main.open",side_effect=OSError("File cannot be written"))
    def test_save_data_when_file_cannot_be_written(self,mock_open_file):
        main.save_data()
        mock_open_file.assert_called_once_with(main.DATA_FILE,"w")

class TestGetMenuChoice(unittest.TestCase):
    @patch("builtins.input", return_value="1")
    def test_valid_menu_choice(self, mock_input):
        result = main.get_menu_choice()
        self.assertEqual(result, 1)

    @patch("builtins.input", return_value="7")
    def test_exit_menu_choice(self, mock_input):
        result = main.get_menu_choice()
        self.assertEqual(result, 7)

    @patch("builtins.input", return_value="abc")
    def test_invalid_menu_choice(self, mock_input):
        result = main.get_menu_choice()
        self.assertIsNone(result)

class TestHandleMenuChoice(unittest.TestCase):
    @patch("src.main.save_data")
    @patch("src.main.add_employee")
    def test_add_employee_menu_choice(self,mock_add_employee,mock_save_data):
        result = main.handle_menu_choice(1)
        mock_add_employee.assert_called_once()
        mock_save_data.assert_called_once()
        self.assertTrue(result)

    @patch("src.main.save_data")
    @patch("src.main.remove_employee")
    def test_remove_employee_menu_choice(self,mock_remove_employee,mock_save_data):
        result = main.handle_menu_choice(2)
        mock_remove_employee.assert_called_once()
        mock_save_data.assert_called_once()
        self.assertTrue(result)

    @patch("src.main.save_data")
    @patch("src.main.update_employee")
    def test_update_employee_menu_choice(self,mock_update_employee,mock_save_data):
        result = main.handle_menu_choice(3)
        mock_update_employee.assert_called_once()
        mock_save_data.assert_called_once()
        self.assertTrue(result)

    @patch("src.main.find_employee")
    def test_find_employee_menu_choice(self,mock_find_employee):
        result = main.handle_menu_choice(4)
        mock_find_employee.assert_called_once()
        self.assertTrue(result)

    @patch("src.main.list_employees")
    def test_list_employee_menu_choice(self,mock_list_employees):
        result = main.handle_menu_choice(5)
        mock_list_employees.assert_called_once()
        self.assertTrue(result)

    @patch("src.main.search_employees")
    def test_search_employee_menu_choice(self,mock_search_employees):
        result = main.handle_menu_choice(6)
        mock_search_employees.assert_called_once()
        self.assertTrue(result)

    @patch("src.main.save_data")
    def test_exit_menu_choice(self, mock_save_data):
        result = main.handle_menu_choice(7)
        mock_save_data.assert_called_once()
        self.assertFalse(result)

    def test_invalid_menu_choice(self):
        result = main.handle_menu_choice(99)
        self.assertTrue(result)

class TestRunApplication(unittest.TestCase):
    @patch("src.main.handle_menu_choice", return_value=False)
    @patch("src.main.get_menu_choice", return_value=7)
    @patch("src.main.display_menu")
    @patch("src.main.load_data")
    def test_application_exits_safely(self,mock_load_data,mock_display_menu,mock_get_menu_choice,mock_handle_menu_choice):
        main.run_application()
        mock_load_data.assert_called_once()
        mock_display_menu.assert_called_once()
        mock_get_menu_choice.assert_called_once()
        mock_handle_menu_choice.assert_called_once_with(7)

if __name__ == "__main__":
    unittest.main()