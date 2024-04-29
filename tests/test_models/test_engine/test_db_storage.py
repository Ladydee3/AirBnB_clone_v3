class TestDBStorageMethods(unittest.TestCase):
    """Tests for the DBStorage class methods"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get(self):
        """Test the get method"""
        # Test case for retrieving an existing object
        new_state = State(name="California")
        models.storage.new(new_state)
        models.storage.save()
        retrieved_state = models.storage.get(State, new_state.id)
        self.assertEqual(retrieved_state, new_state)

        # Test case for retrieving a non-existing object
        non_existing_state = models.storage.get(State, "non_existing_id")
        self.assertIsNone(non_existing_state)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count_all(self):
        """Test count method for all objects"""
        initial_count = models.storage.count()
        new_state = State(name="California")
        models.storage.new(new_state)
        models.storage.save()
        self.assertEqual(models.storage.count(), initial_count + 1)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count_class(self):
        """Test count method for specific class"""
        initial_count = models.storage.count(State)
        new_state = State(name="California")
        models.storage.new(new_state)
        models.storage.save()
        self.assertEqual(models.storage.count(State), initial_count + 1)

