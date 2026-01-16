"""
Student Grade Management System
A real-world example of file handling in Python
"""

import os
STUDENT_FILE = 'students_data.txt'

def add_student():
    """Add a new student with their grades"""
    print("\n--- Add New Student ---")
    name = input("Enter student name: ").strip()
    
    try:
        math = float(input("Enter Math marks: "))
        science = float(input("Enter Science marks: "))
        english = float(input("Enter English marks: "))
        average = (math + science + english) / 3
        
        if average >= 90:
            grade = 'A+'
        elif average >= 80:
            grade = 'A'
        elif average >= 70:
            grade = 'B'
        elif average >= 60:
            grade = 'C'
        else:
            grade = 'F'
        
        # Write to file (append mode)
        with open(STUDENT_FILE, 'a') as file:
            file.write(f"{name},{math},{science},{english},{average:.2f},{grade}\n")
        
        print(f"\n✓ Student {name} added successfully!")
        print(f"Average: {average:.2f}, Grade: {grade}")
        
    except ValueError:
        print(" Invalid input! Please enter numeric values for marks.")
    except Exception as e:
        print(f" Error: {e}")

def view_all_students():
    """Display all student records"""
    print("\n--- All Student Records ---")
    
    try:
        if not os.path.exists(STUDENT_FILE):
            print("No records found. Add students first!")
            return
        
        with open(STUDENT_FILE, 'r') as file:
            lines = file.readlines()
            
            if not lines:
                print("No records found. Add students first!")
                return
            
            print(f"\n{'Name':<20} {'Math':<8} {'Science':<8} {'English':<8} {'Average':<8} {'Grade':<5}")
            print("-" * 65)
            
            for line in lines:
                data = line.strip().split(',')
                name, math, science, english, avg, grade = data
                print(f"{name:<20} {math:<8} {science:<8} {english:<8} {avg:<8} {grade:<5}")
    
    except FileNotFoundError:
        print("No records found. Add students first!")
    except Exception as e:
        print(f" Error reading file: {e}")

def search_student():
    """Search for a specific student"""
    print("\n--- Search Student ---")
    search_name = input("Enter student name to search: ").strip().lower()
    
    try:
        if not os.path.exists(STUDENT_FILE):
            print("No records found!")
            return
        
        found = False
        with open(STUDENT_FILE, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                name = data[0]
                
                if search_name in name.lower():
                    found = True
                    print(f"\n✓ Found: {name}")
                    print(f"Math: {data[1]}, Science: {data[2]}, English: {data[3]}")
                    print(f"Average: {data[4]}, Grade: {data[5]}")
        
        if not found:
            print(f" No student found with name '{search_name}'")
    
    except FileNotFoundError:
        print("No records found!")
    except Exception as e:
        print(f" Error: {e}")

def generate_report():
    """Generate a summary report"""
    print("\n--- Class Report ---")
    
    try:
        if not os.path.exists(STUDENT_FILE):
            print("No records found!")
            return
        
        with open(STUDENT_FILE, 'r') as file:
            lines = file.readlines()
            
            if not lines:
                print("No records found!")
                return
            
            total_students = len(lines)
            total_avg = 0
            grade_count = {'A+': 0, 'A': 0, 'B': 0, 'C': 0, 'F': 0}
            
            for line in lines:
                data = line.strip().split(',')
                total_avg += float(data[4])
                grade_count[data[5]] += 1
            
            class_average = total_avg / total_students
            
            print(f"\nTotal Students: {total_students}")
            print(f"Class Average: {class_average:.2f}")
            print("\nGrade Distribution:")
            for grade, count in grade_count.items():
                print(f"  {grade}: {count} students")
            
            # Save report to a separate file
            with open('class_report.txt', 'w') as report_file:
                report_file.write("=== CLASS PERFORMANCE REPORT ===\n\n")
                report_file.write(f"Total Students: {total_students}\n")
                report_file.write(f"Class Average: {class_average:.2f}\n\n")
                report_file.write("Grade Distribution:\n")
                for grade, count in grade_count.items():
                    report_file.write(f"  {grade}: {count} students\n")
            
            print("\n✓ Report saved to 'class_report.txt'")
    
    except Exception as e:
        print(f"Error: {e}")

def delete_all_records():
    """Delete all student records"""
    confirm = input("\n  Are you sure you want to delete all records? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        try:
            if os.path.exists(STUDENT_FILE):
                os.remove(STUDENT_FILE)
                print("✓ All records deleted successfully!")
            else:
                print("No records to delete.")
        except Exception as e:
            print(f" Error: {e}")
    else:
        print("Deletion cancelled.")

def main():
    """Main menu"""
    while True:
        print("\n" + "="*50)
        print("     STUDENT GRADE MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Generate Class Report")
        print("5. Delete All Records")
        print("6. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            delete_all_records()
        elif choice == '6':
            print("\n👋 Thank you for using the system. Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter a number between 1-6.")
if __name__ == "__main__":
    main()