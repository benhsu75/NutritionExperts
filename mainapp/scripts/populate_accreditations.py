from mainapp.models import *

# def populate_accreditations():
# Delete all existing accreditation
Accreditation.objects.all().delete()

# Add all accreditations
RD = Accreditation(name="RD")
RD.save();

PhD = Accreditation(name="PhD")
PhD.save();

MA = Accreditation(name="MA")
MA.save();

MS = Accreditation(name="MS")
MS.save();

LDN = Accreditation(name="LDN")
LDN.save();

RDN = Accreditation(name="RDN")
RDN.save();

RN = Accreditation(name="RN")
RN.save();

MPH = Accreditation(name="MPH")
MPH.save();

	