# A function that can call itself from within


# def walk(steps):
#     for i in range(steps+1):
#         print(f"You are taking the step #{i}")


def walk(steps):
    if steps < 0:
        return "done"
    
    walk(steps - 1)
    print(f"You are taking the step #{steps}")

walk(3)
