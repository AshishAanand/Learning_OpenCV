import os
import cv2

# Function of CLI interface

def interface() -> None: # Welcome Interface
    print("#####################################")
    print()
    print("Kya Ji, Welcome")
    print()
    print("#####################################")

def main(): # Main working function

    interface() # Welcome interface

    try:
        print("########### [ What do you want to do ] ############")
        print()

        print("1. Open Image")
        print("2. Save Image")

        print()

        # -------------------------

        print("1 -> Open Image and 2 -> Save Image")
        print("####################################")

        user = int(input("Give input: "))

        # Handling imput
        
        if user == 1:
            print()
            img_path = input("Give image absolute path: ")

            image = cv2.imread(img_path) # Reading Image

            # Showing image
            cv2.imshow("Image", image)

        elif user == 2:
            image_path = input("Give a Image path: ")

            new_path = input("Give new path with file name: ")
            print(new_path)

            final_img = cv2.imread(image_path)

            cv2.imwrite(f"{new_path}", final_img)

            saved_image = cv2.imread(new_path)

            cv2.imshow("Your saved image", saved_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()


    except Exception as e:
        print(f"{e}")
    
if __name__ == "__main__":
    main()