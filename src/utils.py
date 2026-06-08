import os
import pickle


def save_object(file_path, obj):
    """Trained objects ko artifacts folder mein serialize/save karne ke liye."""
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

        print(f" [Utils] Object successfully saved at: {file_path}")
    except Exception as e:
        print(f" [Utils] Error saving object: {str(e)}")


def load_object(file_path):
    """Saved components ko computational state mein reload karne ke liye."""
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        print(f" [Utils] Error loading object: {str(e)}")
        return None