#Function 1: Head Printing
def print_head(hair, eye):
    headHair=hair*12
    head1=hair+"|        |"+hair
    head2=hair+"|  "+eye+"  "+eye+"  |"+hair
    head3=" |   /\   |"
    head4=" |        |"
    head5=" \  '--'  /"
    head6="   ------"
    print(headHair)
    print(head1)
    print(head2)
    print(head3)
    print(head4)
    print(head5)
    print(head6)

#Function 2: Body Printing
def print_body(height, arm):
    neck="     XX"
    bodyArm="#"+arm*4+"XX"+arm*4+"#"
    body1="    XXXX"
    print(neck)
    print(bodyArm)
    print((body1+"\n")*height,end="")

#Function 3: Shoe String Reversal
def reverse_shoe(shoe_string):
    reversedShoe = ""
    for char in shoe_string:
        reversedShoe = char + reversedShoe
    return reversedShoe

#Function 4: Leg Printing
def print_legs(height, shoe):
    belt="    ===="
    leg1="   ||  ||"
    shoes1=" "+shoe+"  "+reverse_shoe(shoe)
    print(belt)
    print((leg1+"\n")*height, end="")
    print(shoes1)

#Final Function: Main Function
def main():
    print('Welcome to the custom character creator tool!')
    height = int(input('Overall character height: '))
    hair = input('Character for the hair: ')
    eye = input('Character for the eyes: ')
    arm = input('Character for the arms: ')
    shoe = input('4-character string for the shoes: ')
    segment = (height - 11) // 2
    print()
    print_head(hair, eye)
    print_body(segment, arm)
    print_legs(segment, shoe)

main()