class Map():
    def __init__(self, txt=None, numb=None):
        self.txt = txt
        self.numb = numb

    def file(self, file_path):
        self.txt = [] 
        try:
            with open(file_path, "r") as f:
                for line in f:
                    self.txt.append(line.strip())
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

def calculate_calibration(line):
    first_digit = int(next(char for char in line if char.isdigit()))
    last_digit = int(next(char for char in line[::-1] if char.isdigit()))
    return int(f"{first_digit}{last_digit}")

def main():
    file_path = "Day 1.txt
    search_instance = Map()
    search_instance.file(file_path)

    if search_instance.txt:
        calibration_values = [calculate_calibration(line) for line in search_instance.txt]
        total_sum = sum(calibration_values)

        print("Calibration Values:", calibration_values)
        print("Total Sum:", total_sum)
    else:
        print("No data found in the file.")

if __name__ == "__main__":
    main()