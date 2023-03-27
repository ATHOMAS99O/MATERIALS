import pathlib
import pickle

import face_recognition

DEFAULT_ENCODINGS_PATH = "output/encodings.pkl"

# Create directories if they don't already exist
pathlib.Path("training").mkdir(exist_ok=True)
pathlib.Path("output").mkdir(exist_ok=True)
pathlib.Path("validation").mkdir(exist_ok=True)


def encode_known_faces(
    model: str = "hog", encodings_location: str = DEFAULT_ENCODINGS_PATH
) -> None:
    """
    Loads images in the training directory and builds a dictionary of their
    names and encodings.
    """
    names = []
    encodings = []
    for filepath in pathlib.Path("training").glob("*/*"):
        name = filepath.parent.name
        image = face_recognition.load_image_file(filepath)

        face_locations = face_recognition.face_locations(image, model=model)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)

    name_encodings = {"names": names, "encodings": encodings}
    with open(encodings_location, "wb") as f:
        pickle.dump(name_encodings, f)


encode_known_faces()
