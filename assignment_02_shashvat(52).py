# DECORATORS
# Used to add extra functionality to a function without modifying it.

def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "**" + result + "**"
    return wrapper

def add_border(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        border = "-" * 40
        return border + "\n" + result + "\n" + border
    return wrapper


# CLASSMETHOD
# Works with the class (cls) instead of an object (self).

class Report:

    # Shared by all objects of the class.
    templates = {}

    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author
        self.sections = []

    # Saves a template for future reports.
    @classmethod
    def add_template(cls, name, section_list):
        cls.templates[name] = section_list
        print(f"Template '{name}' saved with sections: {section_list}")

    # Creates a report using a saved template.
    @classmethod
    def create_from_template(cls, template_name, title, author="Unknown"):
        new_report = cls(title, author)
        for heading in cls.templates[template_name]:
            new_report.add_section(heading, "content not filled yet")
        return new_report

    # Adds a new section.
    def add_section(self, heading, content):
        self.sections.append((heading, content))

    # Updates an existing section.
    def fill_section(self, heading, content):
        for i in range(len(self.sections)):
            if self.sections[i][0] == heading:
                self.sections[i] = (heading, content)
                return True
        return False


# MAGIC METHODS (DUNDER METHODS)
# Special methods automatically called by Python.

    @bold
    @add_border
    def summary(self):
        return f"Report: {self.title} | Author: {self.author} | Sections: {len(self.sections)}"

    # Used by print(object)
    def __str__(self):
        text = f"REPORT: {self.title} (by {self.author})\n"
        for heading, content in self.sections:
            text += f" - {heading}: {content}\n"
        return text

    # Used by len(object)
    def __len__(self):
        return len(self.sections)

    # Used by object[index]
    def __getitem__(self, index):
        return self.sections[index]

    # Used by object1 + object2
    def __add__(self, other):
        combined = Report(self.title + " + " + other.title, self.author)
        combined.sections = self.sections + other.sections
        return combined

    # Used by object1 == object2
    def __eq__(self, other):
        return self.title == other.title and self.sections == other.sections


# DEMO

if __name__ == "__main__":

    # Save a template.
    Report.add_template("project_report", ["Introduction", "Result", "Conclusion"])

    # Create report from template.
    r1 = Report.create_from_template("project_report", "My Mini Project", "Rahul")
    r1.fill_section("Introduction", "This project shows OOP concepts in Python.")
    r1.fill_section("Result", "The program worked correctly.")
    r1.fill_section("Conclusion", "Decorators and magic methods make code flexible.")

    # Create another report.
    r2 = Report("Attendance Report", "Rahul")
    r2.add_section("Summary", "92% attendance this month.")

    # Magic methods demonstration.
    print(r1)
    print(len(r1))
    print(r1[0])

    combined = r1 + r2
    print(combined)

    print(r1 == r1)

    # Decorator demonstration.
    print(r1.summary())