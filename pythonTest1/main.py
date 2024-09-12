# Write a function for each subtask
# Task 1.
# Write a Python program to create a list containing the following
# numbers: 10, 20, 30, 40, 50.
#               sub-task1: Print the list.
def task1():
    """
    Functia printeza lista
    :return:
    """
    print("Task 1")
    list1 = [10, 20, 30, 40, 50]
    print("sub-task1:", list1)

# Task 2.
# Given the list
#       numbers = [10, 20, 30, 40, 50],
#
#       write a Python program to:
#       sub-task2: Print the first element of the list.
#       sub-task4: Print the third element of the list.
#       sub-task5: Change the second element of the list to 25 and print the updated list.
#       sub-task6: Insert the number 15 at the second position in the list

def task2():
    """
    Functia printeaza primul si ultimul element, apoi schimba al doilea in 25 si la final introduce numarul 15 in a 2a
    pozitie
    :return:
    """
    print("Task 2")
    numbers = [10, 20, 30, 40, 50]
    print("sub-task2:", numbers[0])
    print("sub-task4:", numbers[2])
    numbers[1] = 25
    print("sub-task5:", numbers)
    numbers.insert(1, 15)
    print("sub-task6:", numbers)
def sub_task3():
    """
    o functie care nu face nimic
    :return:
    """
    print("Sub task 3")
    pass



# Task 3.
# Given the list
#       matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],
#
#       write a Python program to:
#       sub-task7: Print the second element of the second list.
#       sub-task8: Print all the elements from the first, third and last list.
def task3():
    """
    O functie care printeaza al 2 lea element al listei si primul, al 3lea si ultimul
    :return:
    """
    print("Task 3")
    matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    print("sub-task7:", matrix[1])
    first = matrix[0]
    third = matrix[2]
    last = matrix[-1]
    print("sub-task8:")
    print("First elem is ", first)
    print("Third elem is", third)
    print("Last elem is", last)


# Task 4.
# Write a Python program to create a dictionary with the following key-value pairs
#       sub-task9: Print the dictionary
# Given the following dictionary
#       person = {"name": "Alice", "age": 25, "city": "New York"},
#
#       write a Python program to:
#       sub-task9: Print the value associated with the key "name".
#       sub-task10: Print the value associated with the key "age".
#       sub-task11: Print the value of the "city" key using the get() method.
def task4():
    """
    O functie care printeaza valoarea cheilor"name", "age" si cu ajutorul metodei get() a valorii "city"
    :return:
    """
    print("Task4")
    person ={
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }
    print("sub-task9:", person["name"])
    print("sub-task10:", person["age"])
    city_value = person.get("city")
    print("sub-task11:", city_value)

# Task 5.
# Write a Python program that takes a list of fruits:
#       fruits = ["apple", "banana", "cherry", "apple", "banana", "apple"]

#       sub-task12: Create a dictionary that counts the number of occurrences of each fruit, resulting in:
#           {"apple": 3, "banana": 2, "cherry": 1}
def task5():
    """
    O functie care numara de cate ori apare fiecare frunct in lista
    :return:
    """
    print("Task 5")
    fruits = ["apple", "banana", "cherry", "apple", "banana", "apple"]
    fruits_count = {}
    for fruit in fruits:
        if fruit in fruits_count:
            fruits_count[fruit] += 1
        else:
            fruits_count[fruit] = 1
    print("sub-task12:", fruits_count)



if __name__ == "__main__":
    print("Welcome to the first test of the course!")
    task1()
    task2()
    sub_task3()
    task3()
    task4()
    task5()