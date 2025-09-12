from storages.backends.azure_storage import AzureStorage
import os

class AzureMediaStorage(AzureStorage):
    account_name = os.getenv("AZURE_ACCOUNT_NAME")
    account_key = os.getenv("AZURE_ACCOUNT_KEY")
    azure_container = os.getenv("AZURE_CONTAINER")
    expiration_secs = None
    location = 'media'

    def get_available_name(self, name, max_length=None):
        """
        To use always the same name.
        """
        if self.exists(name):
            self.delete(name)
        return name   