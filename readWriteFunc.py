def write_to_file():
    file_object = open("playlist.txt", mode="w") 
    #file_object = open("playlist.txt", mode="a") 
    file_object.write("Twinkle, twinkle, little star,\n")
    file_object.write("How I wonder what you are!\n")
    file_object.write("Up above the world so high,\n")
    file_object.write("Like a diamond in the sky.\n")
    file_object.close()




def read_file():
    """Example of reading in a whole file"""
    file_object = open("playlist.txt", mode="r")
    rhyme = file_object.read()
    print(file_object.read(),"here")
    file_object.close()
    print(rhyme, "here2")

write_to_file()  
read_file()
