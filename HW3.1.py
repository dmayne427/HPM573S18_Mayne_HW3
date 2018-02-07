# create the class Patient
class Patient:
    def __init__(self, name):
        """
        :param name: name of patient
        """
        self.name = name

    def discharge(self):
        """ abstract method to be overridden in derived classes
        :returns name and type of patient """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

# create the subclass EmergencyPatient
class EmergencyPatient(Patient):
        def __init__(self, name):
            Patient.__init__(self, name)
            self.ecost = 1000
        def discharge(self):
            print(self.name, "Emergency")


# create the subclass HospitalizedPatient
class HospitalizedPatient(Patient):
        def __init__(self, name):
            Patient.__init__(self, name)
            self.ecost=2000
        def discharge(self):
            print(self.name, "Hospitalized")

# create the class Hospital
class Hospital:
    def __init__(self):
        self.patients = []
        self.cost = 0

    def admit(self, patients):
        self.patients.append(patients)

    def discharge_all(self):
        for patients in self.patients:
            patients.discharge()
            self.cost+=patients.ecost

    def get_total_cost(self):
        return self.cost

P1=HospitalizedPatient("P1")
P2=HospitalizedPatient("P2")
P3=EmergencyPatient("P3")
P4=EmergencyPatient("P4")
P5=EmergencyPatient("P5")

YNHH=Hospital()
YNHH.admit(P1)
YNHH.admit(P2)
YNHH.admit(P3)
YNHH.admit(P4)
YNHH.admit(P5)

YNHH.discharge_all()
print(YNHH.get_total_cost())

