

def main():
    print("""
     _____       _   _                           
    |  __ \\     | | | |                          
    | |__) |   _| |_| |__   ___  _ __            
    |  ___/ | | | __| '_ \\ / _ \\| '_ \\           
    | |   | |_| | |_| | | | (_) | | | |          
  _ |_|_   \\__, |\\__|_| |_|\\___/|_| |_|          
 | |  | |   __/ |                                
 | |__| | _|___/ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |                      
                     |___/                       \n\n"""

    )

    print("Enter your name to start:")
    name = input("What is your name?\n")
    print(f"\nHello {name}, Let's begin shall we?")
    print("But first, I need to know if you want this to be Easy, medium or hard?")
    
    while True:
        difficulty = input("What difficulty do you want? Easy, Medium or Hard?\n").lower()
        if difficulty in ("easy", "medium", "hard"):
            break
        print("Invalid choice! Please enter : Easy, Medium or Hard.\n")


if __name__ == "__main__":
    main()
