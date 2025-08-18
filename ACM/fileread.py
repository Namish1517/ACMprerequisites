def count_words(input_file,output_file):
    try:
        with open(input_file,"r")as f:
            text=f.read()
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading '{input_file}':{e}")
        return 
    text=text.lower()  
    words=text.split()  
    frequency={}
    for word in words:
        frequency[word]=frequency.get(word,0)+1
    try:
        with open(output_file,"w")as f:
            for word,count in sorted(frequency.items()):
                f.write(f"{word}:{count}\n")
    except Exception as e:
        print(f"Error writing to '{output_file}': {e}")
if __name__=="__main__":
    input_filename=input("Enter the name of the file to read from:").strip()
    output_filename=input("Enter the name of the file to save results to:").strip()
    count_words(input_filename,output_filename)