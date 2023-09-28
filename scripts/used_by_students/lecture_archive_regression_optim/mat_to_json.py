import scipy.io
import numpy as np
import json

def mat_to_json(mat_filepath, json_filepath):
    """
    Converts .mat file to .json file.

    :param mat_filepath: path to the input .mat file
    :param json_filepath: path to the output .json file
    """
    # Load the .mat file
    mat_data = scipy.io.loadmat(mat_filepath)

    # Prepare data for json dump.
    # Note: This converts numpy arrays to lists
    data = {}
    for i, (key, value) in enumerate(mat_data.items()):
        # Skip keys that are internals of .mat format
        if key.startswith('__') or key.startswith('_'):
            continue
        data[key+str(i)] = value.tolist()
        

    # Write data to json file
    with open(json_filepath, 'w') as outfile:
        json.dump(data, outfile)

import scipy.io

def mat_to_txt(mat_filepath, txt_filepath):
    """
    Converts .mat file to .txt file.

    :param mat_filepath: path to the input .mat file
    :param txt_filepath: path to the output .txt file
    """
    # Load the .mat file
    mat_data = scipy.io.loadmat(mat_filepath)

    keys = []
    cols = []
    for i, (key, value) in enumerate(mat_data.items()):
        # Skip keys that are internal to .mat format
        if key.startswith('__') or key.startswith('_'):
            continue

        # Write the key as header
        keys.append(f"{key}{i}")

        # Assume value is a list of lists (2D array) and write each sub-list as a row
        cols.append(value.ravel().tolist())
    with open(txt_filepath, 'w') as outfile:
        outfile.write("\t".join(keys))
        # Iterate through each item
        for row in zip(*np.array(cols)):
            outfile.write("\n")
            outfile.write("\t".join(map(str, row)))
    

# Example usage:
mat_to_txt('tudataset1.mat', 'tudataset1.txt')


# Example usage:
mat_to_json('tudataset1.mat', 'tudataset1.json')
