import unittest
from models.engine.file_storage import FileStorage

class TestFileStorageMethods(unittest.TestCase):
    def setUp(self):
        # Create an instance of FileStorage
        self.storage = FileStorage()

    def tearDown(self):
        # Reset the storage dictionary to an empty state after each test
        self.storage._FileStorage__objects = {}

    def test_save_and_reload(self):
        # Create some sample data
        obj = BaseModel()
        obj1 = BaseModel()

        sample_data = {
            'SampleModel.123': {'name': 'SampleObject1'},
            'SampleModel.456': {'name': 'SampleObject2'}
        }

        # Add the sample data to the storage dictionary
        self.storage._FileStorage__objects = sample_data

        # Save the data to a file
        self.storage.save()

        # Clear the storage dictionary
        self.storage._FileStorage__objects = {}

        # Reload the data from the file
        self.storage.reload()

        # Verify that the data was successfully reloaded
        self.assertEqual(self.storage.all(), sample_data)

if __name__ == '__main__':
    unittest.main()

