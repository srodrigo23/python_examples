# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    i = 1
    path = "/Users/sergiorodrigo/Documents/images/"
    for filename in os.listdir(path): 
        dst = path + "g" + str(i) + ".png"
        src = path + filename 
        #dst ='xyz'+ dst 
        #rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 

    # Calling main() function 
    main() 