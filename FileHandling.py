 #File Handling
import OOPS # Importing module for object-oriented programming concepts

class FileHandling:
    def read_file(self, file_path): # Method to read a file
        try:
            with open(file_path, 'r') as file: # Open file in read mode
                content = file.read() # Read the first line of the file
                print("File Content:")
                print(content)
        except FileNotFoundError:
            print(f"Error: The file at {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

    def write_file(self, file_path, data):
        try:
            with open(file_path, 'w') as file: # Open file in append mode
                file.write(data)
                print(f"Data written to {file_path} successfully.")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            
# r,w,a,x,b,t 
# r -> read
# w -> write
# a -> append
# x -> create
# b -> binary
# t -> text          
