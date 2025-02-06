# Write a python program to create a function that returns smallest value from the given text file.

def smallest(filename):
    try:
        with open(filename, 'r') as file:
            smallest = None
            for line in file:
                line = line.strip()  
                if not line:  
                    continue
                try:
                    value = float(line)  
                    if smallest is None or value < smallest:
                        smallest = value
                except ValueError:
                    try: 
                        value = int(line)
                        if smallest is None or value < smallest:
                            smallest = value
                    except ValueError:
                        if smallest is None:
                            smallest = line
                        elif isinstance(smallest, str) and line < smallest:
                            smallest = line
            return smallest
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
with open('file4.txt','w') as f4:
    f4.write('71\n')
    f4.write('12\n')
    f4.write('55\n')
    f4.write('1\n')
    f4.write('32\n')
print("Smallest value: ",smallest('file4.txt'))