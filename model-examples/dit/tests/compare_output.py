import numpy as np

def load_npy_file(file_path):
    return np.load(file_path)

def calculate_mae(output1, output2):
    return np.mean(np.abs(output1 - output2))

def main():
    ms_output = load_npy_file("ms_output.npy")
    pt_output = load_npy_file("pt_output.npy")

    mae = calculate_mae(ms_output, pt_output)
    relative_mae = np.mean(np.abs(ms_output - pt_output) / (np.abs(pt_output) + 1e-8))

    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Relative MAE (ms relative to pt): {relative_mae}")

    if mae < 0.002 and relative_mae < 0.02:
        print("The mae is less than 0.002 and the relative mae is less than 2%, the model is correct.")

if __name__ == "__main__":
    main()
