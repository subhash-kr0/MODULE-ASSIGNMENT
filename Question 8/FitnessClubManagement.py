class Member:
    _id_counter = 1  # Class-level attribute to generate unique IDs
    
    def __init__(self, name, age, membership_type):
        self._id = Member._id_counter  # Unique ID
        Member._id_counter += 1
        self.name = name
        self.age = age
        self.membership_type = membership_type
        self._membership_status = "Active"  # Private attribute for membership status

    def register_member(self):
        print(f"Member {self.name} registered with {self.membership_type} membership.")

    def renew_membership(self):
        if self._membership_status == "Cancelled":
            print(f"Cannot renew a cancelled membership for {self.name}.")
        else:
            print(f"Membership for {self.name} has been renewed.")
            self._membership_status = "Active"

    def cancel_membership(self):
        if self._membership_status == "Active":
            self._membership_status = "Cancelled"
            print(f"Membership for {self.name} has been cancelled.")
        else:
            print(f"Membership for {self.name} is already cancelled.")

    def get_id(self):
        return self._id

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.membership_type} membership - Status: {self._membership_status}"


class FamilyMember(Member):
    def __init__(self, name, age, membership_type, family_size):
        super().__init__(name, age, membership_type)
        self.family_size = family_size

    def register_member(self):
        print(f"Family membership for {self.name} (Family size: {self.family_size}) registered.")

    def __str__(self):
        return super().__str__() + f" (Family size: {self.family_size})"


class IndividualMember(Member):
    def __init__(self, name, age, membership_type, personal_trainer=False):
        super().__init__(name, age, membership_type)
        self.personal_trainer = personal_trainer

    def register_member(self):
        trainer_str = "with a personal trainer" if self.personal_trainer else "without a personal trainer"
        print(f"Individual membership for {self.name} registered {trainer_str}.")

    def __str__(self):
        trainer_str = "with Personal Trainer" if self.personal_trainer else "without Personal Trainer"
        return super().__str__() + f" ({trainer_str})"


class FitnessClub:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)
        member.register_member()

    def renew_member(self, member_id):
        for member in self.members:
            if member.get_id() == member_id:
                member.renew_membership()
                return
        print(f"Member with ID {member_id} not found.")

    def cancel_member(self, member_id):
        for member in self.members:
            if member.get_id() == member_id:
                member.cancel_membership()
                return
        print(f"Member with ID {member_id} not found.")

    def display_members(self):
        print("Members:")
        for member in self.members:
            print(member)


# Testing the Fitness Club Management System

# Create the fitness club
fitness_club = FitnessClub()

# Add members
individual_member = IndividualMember(name="John Doe", age=30, membership_type="Individual", personal_trainer=True)
family_member = FamilyMember(name="Jane Smith", age=40, membership_type="Family", family_size=4)
fitness_club.add_member(individual_member)
fitness_club.add_member(family_member)

# Display members
fitness_club.display_members()

# Manage memberships
fitness_club.renew_member(individual_member.get_id())
fitness_club.cancel_member(family_member.get_id())
fitness_club.renew_member(family_member.get_id())  # Trying to renew a cancelled membership
fitness_club.cancel_member(individual_member.get_id())

# Display members after updates
fitness_club.display_members()
