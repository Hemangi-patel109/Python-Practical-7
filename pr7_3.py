# A text file contains a header line, few comments lines followed by actual lines of data. Write a python program to create a function skip_header() that skips the header and all the comment lines and prints only actual lines of data.

def skip_header(filename):
    try:
        with open(filename, 'r') as file3:
            for line in file3:
                line = line.strip()  
                if not line:  
                    continue
                if line.startswith('#'):  
                    continue
                if hasattr(skip_header, "header_skipped"): 
                    print(line)
                else:
                    skip_header.header_skipped = True 
                    continue 
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

with open("file3.txt", "w") as f:
    f.write("Name,Age,City\n")  
    f.write("# This is a comment line\n")
    f.write("# Another comment\n")
    f.write("Hemangi,20,Gandhinagar\n")
    f.write("Adrien,15,Paris\n")
    f.write("Marinette,14,Paris\n")

skip_header("file3.txt")