"""
01. Write a program that displays your information : Your name, Full_Address, Mobile Number, college name, Course Subjects
"""

def intro():
    info = {
        "Name": "Sameer Ali Khan",
        "Address": "Maneru Hostel",
        "Contact Number": "9986547123",
        "College Name": "UCS, OU",
        "Course": "M.Sc",
        "Subjects": [
            "Design & Analysis of Algorithms",
            "Python",
            "Computer Networks",
            "Automata Theory"
        ]
    }

    for key, value in info.items():
        if isinstance(value, list):
            print(f"{key} :")
            for item in value:
                print(f"  - {item}")
        else:
            print(f"{key} : {value}")

intro()
