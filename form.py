from flask import Flask, request, render_template
import pandas as pd
from pathlib import Path

# Flask constructor
app = Flask(__name__)  

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def recordsdata():
    if request.method == "POST":
       TotalMedline = request.form.get("TotalMedline")
       AgricultureTopic = request.form.get("AgricultureTopic")
       AlliedTopic = request.form.get("AlliedTopic")
       BiochemistryTopic = request.form.get("BiochemistryTopic")
       BusinessTopic = request.form.get("BusinessTopic")
       DentistryTopic = request.form.get("DentistryTopic")
       DrugsTopic = request.form.get("DrugsTopic")
       EcologyTopic = request.form.get("EcologyTopic")
       EducationTopic = request.form.get("EducationTopic")
       EngineeringTopic = request.form.get("EngineeringTopic")
       EnvironmentalTopic = request.form.get("EnvironmentalTopic")
       MedicineTopic = request.form.get("MedicineTopic")
       NursingTopic = request.form.get("NursingTopic")
       PhysicalTopic = request.form.get("PhysicalTopic")
       PsychologyTopic = request.form.get("PsychologyTopic")
       SportsTopic = request.form.get("SportsTopic")
       VeterinaryTopic = request.form.get("VeterinaryTopic")
       
       ArtTopic = request.form.get("ArtTopic")
       AudiologyTopic = request.form.get("AudiologyTopic")
       DieteticsTopic = request.form.get("DieteticsTopic") 
       ImagingTopic = request.form.get("ImagingTopic") 
       OccupationalTopic = request.form.get("OccupationalTopic")
       PhysiotherapyTopic = request.form.get("PhysiotherapyTopic")
       PrehospitalTopic = request.form.get("PrehospitalTopic")
       ProstheticsTopic = request.form.get("ProstheticsTopic")
       RecreationTopic = request.form.get("RecreationTopic")
       RespiratoryTherapyTopic = request.form.get("RespiratoryTherapyTopic")
       SocialTopic = request.form.get("SocialTopic")
       SpiritualTopic = request.form.get("SpiritualTopic")

       
       
       
       BloodTopic = request.form.get("BloodTopic")
       CancerTopic = request.form.get("CancerTopic")
       CardiovascularTopic = request.form.get("CardiovascularTopic")
       ComplementaryTopic = request.form.get("ComplementaryTopic")
       CongenitalTopic = request.form.get("CongenitalTopic")
       EarTopic = request.form.get("EarTopic")
       EyeTopic = request.form.get("EyeTopic")
       GeriatricsTopic = request.form.get("GeriatricsTopic")
       InfectionTopic = request.form.get("InfectionTopic")
       InflammatoryTopic = request.form.get("InflammatoryTopic")
       InjuriesTopic = request.form.get("InjuriesTopic")
       MetabolicTopic = request.form.get("MetabolicTopic")
       MusculoskeletalTopic = request.form.get("MusculoskeletalTopic")
       NeurologicalTopic = request.form.get("NeurologicalTopic")
       OralTopic = request.form.get("OralTopic")
       PediatricsTopic = request.form.get("PediatricsTopic")
       RenalTopic = request.form.get("RenalTopic")
       ReproductiveTopic = request.form.get("ReproductiveTopic")
       RespiratoryTopic = request.form.get("RespiratoryTopic")
       SkinTopic = request.form.get("SkinTopic")
       SleepTopic = request.form.get("SleepTopic")
       StrokeTopic = request.form.get("StrokeTopic")
       SurgeryTopic = request.form.get("SurgeryTopic")
       GeneralTopic = request.form.get("GeneralTopic")
       
 
       CINAHLDatabase = request.form.get("CINAHL")
       EmbaseDatabase = request.form.get("Embase")
       ScopusDatabase = request.form.get("Scopus")
       CochraneLibraryDatabase = request.form.get("CochraneLibrary")
       CochraneCentralDatabase = request.form.get("CochraneCentral")
       ERICDatabase = request.form.get("ERIC")
       PEDroDatabase = request.form.get("PEDro")
       PsycINFODatabase = request.form.get("PsycINFO")
       WebOfScienceDatabase = request.form.get("Web of Science")
       
       DatabaseSelection1 = request.form.get("DatabaseSelection1")
       DatabaseSelection2 = request.form.get("DatabaseSelection2")
       DatabaseSelection3 = request.form.get("DatabaseSelection3")
       DatabaseSelection4 = request.form.get("DatabaseSelection4")
       DatabaseSelection5 = request.form.get("DatabaseSelection5")
       DatabaseSelection6 = request.form.get("DatabaseSelection6")
       DatabaseSelection7 = request.form.get("DatabaseSelection7")
       DatabaseSelection8 = request.form.get("DatabaseSelection8")
       DatabaseSelection9 = request.form.get("DatabaseSelection9")
       DatabaseSelection10 = request.form.get("DatabaseSelection10")
            
       Topics = []
 
       TotalMedline = float(TotalMedline) 


       if AgricultureTopic=="on":
           Topics.append("Agriculture")
       if AlliedTopic=="on":
           Topics.append("Allied Health")
           AlliedDisplay = ""
       else:
           AlliedDisplay = "display: none;"
       if BiochemistryTopic=="on":
           Topics.append("Biochemistry, Genetics, and Microbiology")
       if BusinessTopic=="on":
           Topics.append("Business and Economics")
       if DentistryTopic=="on":
           Topics.append("Dentistry")
       if DrugsTopic=="on":
           Topics.append("Drugs and Supplements (not toxicology)")    
       if EcologyTopic=="on":
           Topics.append("Ecology and Zoology")
       if EducationTopic=="on":
           Topics.append("Education")
       if EngineeringTopic=="on":
           Topics.append("Engineering")
       if EnvironmentalTopic=="on":
           Topics.append("Environmental Science")
       if MedicineTopic=="on":
           Topics.append("Medicine")
           MedicineDisplay = ""
       else:
           MedicineDisplay = "display: none;"
       if NursingTopic=="on":
           Topics.append("Nursing")
       if PhysicalTopic=="on":
           Topics.append("Physical Sciences and Mathematics")
       if PsychologyTopic=="on":
           Topics.append("Psychology, Psychiatry, and Mental Health")
       if SportsTopic=="on":
           Topics.append("Sports and Recreation")
       if VeterinaryTopic=="on":
           Topics.append("Veterinary")

       if ArtTopic=="on":
           Topics.append("Art/music/drama therapy")
       if AudiologyTopic=="on":
           Topics.append("Audiology and speech-language pathology")
       if DieteticsTopic=="on":
           Topics.append("Dietetics")
       if ImagingTopic=="on":
           Topics.append("Imaging")
       if OccupationalTopic=="on":
           Topics.append("Occupational therapy")
       if PhysiotherapyTopic=="on":
           Topics.append("Physiotherapy")
       if PrehospitalTopic=="on":
           Topics.append("Prehospital care")
       if ProstheticsTopic=="on":
           Topics.append("Prosthetics and orthotics")
       if RecreationTopic=="on":
           Topics.append("Recreation therapy")
       if RespiratoryTherapyTopic=="on":
           Topics.append("Respiratory therapy")
       if SocialTopic=="on":
           Topics.append("Social work")
       if SpiritualTopic=="on":
           Topics.append("Spiritual care")

       if BloodTopic=="on":
           Topics.append("Blood and hematology")
       if CancerTopic=="on":
           Topics.append("Cancer")
       if CardiovascularTopic=="on":
           Topics.append("Cardiovascular")
       if ComplementaryTopic=="on":
           Topics.append("Complementary and alternative medicine")
       if CongenitalTopic=="on":
           Topics.append("Congenital disorders")
       if EarTopic=="on":
           Topics.append("Ear and hearing")
       if EyeTopic=="on":
           Topics.append("Eye and vision")
       if GeriatricsTopic=="on":
           Topics.append("Geriatrics and gerontology")
       if InfectionTopic=="on":
           Topics.append("Infection")
       if InflammatoryTopic=="on":
           Topics.append("Inflammatory and immune system")
       if InjuriesTopic=="on":
           Topics.append("Injuries and accidents")
       if MetabolicTopic=="on":
           Topics.append("Metabolic and endocrine")
       if MusculoskeletalTopic=="on":
           Topics.append("Musculoskeletal")
       if NeurologicalTopic=="on":
           Topics.append("Neurological")
       if OralTopic=="on":
           Topics.append("Oral and gastrointestinal")
       if PediatricsTopic=="on":
           Topics.append("Pediatrics and neonatology")
       if RenalTopic=="on":
           Topics.append("Renal, gynecological and urogenital")
       if ReproductiveTopic=="on":
           Topics.append("Reproductive health and childbirth")
       if RespiratoryTopic=="on":
           Topics.append("Respiratory")
       if SkinTopic=="on":
           Topics.append("Skin")
       if SleepTopic=="on":
           Topics.append("Sleep")
       if StrokeTopic=="on":
           Topics.append("Stroke")
       if SurgeryTopic=="on":
           Topics.append("Surgery")
       if GeneralTopic=="on":
           Topics.append("General and public health and safety")

       Topics = "; ".join(Topics)
       print(Topics)
       
       pd.options.display.float_format = '{:.0f}'.format
       EXCEL_FILE_PATH = Path.cwd() / 'SR Calculator Sample Data.xlsx'
       df = pd.read_excel(EXCEL_FILE_PATH)
       df.head()

       if DatabaseSelection1=="selectone":
           display1 = "display: none;"
           DatabaseSelection1 = ""
           DatabaseSelection1Records = "Not selected"
       elif DatabaseSelection1==None:
           display1 = "display: none;"
           DatabaseSelection1 = ""
           DatabaseSelection1Records = "Not selected"
       else:
           display1 = ""
           DatabaseSelection1Average = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')[DatabaseSelection1].mean()
           if pd.isna(DatabaseSelection1Average):
                DatabaseSelection1Records = "No data"
           else:
                DatabaseSelection1Records = DatabaseSelection1Average.round(0)

       if DatabaseSelection2=="selectone":
           display2 = "display: none;"
           DatabaseSelection2 = ""
           DatabaseSelection2Records = "Not selected"
       elif DatabaseSelection2==None:
           display2 = "display: none;"
           DatabaseSelection2 = ""
           DatabaseSelection2Records = "Not selected"
       else:
           display2 = ""
           DatabaseSelection2Average = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')[DatabaseSelection2].mean()
           if pd.isna(DatabaseSelection2Average):
                DatabaseSelection2Records = "No data"
           else:
                DatabaseSelection2Records = DatabaseSelection1Average.round(0)

       if DatabaseSelection3=="selectone":
           display3 = "display: none;"
           DatabaseSelection = ""
           DatabaseSelection3Records = "Not selected"
       elif DatabaseSelection3==None:
           display3 = "display: none;"
           DatabaseSelection3 = ""
           DatabaseSelection3Records = "Not selected"
       else:
           display3 = ""
           DatabaseSelection3Average = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')[DatabaseSelection3].mean()
           if pd.isna(DatabaseSelection3Average):
                DatabaseSelection3Records = "No data"
           else:
                DatabaseSelection3Records = DatabaseSelection3Average.round(0)      

       if DatabaseSelection4=="selectone":
           display4 = "display: none;"
           DatabaseSelection4 = ""
           DatabaseSelection4Records = "Not selected"
       elif DatabaseSelection4==None:
           display4 = "display: none;"
           DatabaseSelection4 = ""
           DatabaseSelection4Records = "Not selected"
       else:
           display4 = ""
           DatabaseSelection4Average = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')[DatabaseSelection4].mean()
           if pd.isna(DatabaseSelection4Average):
                DatabaseSelection4Records = "No data"
           else:
                DatabaseSelection4Records = DatabaseSelection4Average.round(0)
 
       if DatabaseSelection5=="selectone":
           display5 = "display: none;"
           DatabaseSelection5 = ""
           DatabaseSelection5Records = "Not selected"
       elif DatabaseSelection5==None:
           display5 = "display: none;"
           DatabaseSelection5 = ""
           DatabaseSelection5Records = "Not selected"
       else:
           display5 = ""
           DatabaseSelection5Average = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')[DatabaseSelection5].mean()
           if pd.isna(DatabaseSelection5Average):
                DatabaseSelection5Records = "No data"
           else:
                DatabaseSelection5Records = DatabaseSelection5Average.round(0)
 
       if DatabaseSelection6=="selectone":
           display6 = "display: none;"
           DatabaseSelection6 = ""
           DatabaseSelection6Records = "Not selected"
       elif DatabaseSelection6==None:
           display6 = "display: none;"
           DatabaseSelection6 = ""
           DatabaseSelection6Records = "Not selected"
       else:
           display6 = ""
           DatabaseSelection6Average = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')[DatabaseSelection6].mean()
           if pd.isna(DatabaseSelection6Average):
                DatabaseSelection6Records = "No data"
           else:
                DatabaseSelection6Records = DatabaseSelection6Average.round(0)
 
       if DatabaseSelection7=="selectone":
           display7 = "display: none;"
           DatabaseSelection7 = ""
           DatabaseSelection7Records = "Not selected"
       elif DatabaseSelection7==None:
           display7 = "display: none;"
           DatabaseSelection7 = ""
           DatabaseSelection7Records = "Not selected"
       else:
           display7 = ""
           DatabaseSelection7Average = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')[DatabaseSelection7].mean()
           if pd.isna(DatabaseSelection7Average):
                DatabaseSelection7Records = "No data"
           else:
                DatabaseSelection7Records = DatabaseSelection7Average.round(0)
 
       if DatabaseSelection8=="selectone":
           display8 = "display: none;"
           DatabaseSelection8 = ""
           DatabaseSelection8Records = "Not selected"
       elif DatabaseSelection8==None:
           display8 = "display: none;"
           DatabaseSelection8 = ""
           DatabaseSelection8Records = "Not selected"
       else:
           display8 = ""
           DatabaseSelection8Average = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')[DatabaseSelection8].mean()
           if pd.isna(DatabaseSelection8Average):
                DatabaseSelection8Records = "No data"
           else:
                DatabaseSelection8Records = DatabaseSelection8Average.round(0)

       if DatabaseSelection9=="selectone":
           display9 = "display: none;"
           DatabaseSelection9 = ""
           DatabaseSelection9Records = "Not selected"
       elif DatabaseSelection9==None:
           display9 = "display: none;"
           DatabaseSelection9 = ""
           DatabaseSelection9Records = "Not selected"
       else:
           display9 = ""
           DatabaseSelection9Average = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')[DatabaseSelection9].mean()
           if pd.isna(DatabaseSelection9Average):
                DatabaseSelection9Records = "No data"
           else:
                DatabaseSelection9Records = DatabaseSelection9Average.round(0)
 
       if DatabaseSelection10=="selectone":
           display10 = "display: none;"
           DatabaseSelection10 = ""
           DatabaseSelection10Records = "Not selected"
       elif DatabaseSelection10==None:
           display10 = "display: none;"
           DatabaseSelection10 = ""
           DatabaseSelection10Records = "Not selected"
       else:
           display10 = ""
           DatabaseSelection10Average = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')[DatabaseSelection10].mean()
           if pd.isna(DatabaseSelection10Average):
                DatabaseSelection10Records = "No data"
           else:
                DatabaseSelection10Records = DatabaseSelection10Average.round(0)

       if CINAHLDatabase=="on":
           CINAHLAverage = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')['CINAHL'].mean()
           if pd.isna(CINAHLAverage):
                CINAHLAverage = "No data"
           else:
                CINAHLAverage = CINAHLAverage.round(0)

       else:
           CINAHLAverage = "Not selected"

       if EmbaseDatabase=="on":
           EmbaseAverage = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')['Embase'].mean()
           if pd.isna(EmbaseAverage):
                EmbaseAverage = "No data"
           else:
                EmbaseAverage = EmbaseAverage.round(0)

       else:
           EmbaseAverage = "Not selected"

       if ScopusDatabase=="on":
           ScopusAverage = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')['Scopus'].mean()
           if pd.isna(ScopusAverage):
                ScopusAverage = "No data"
           else:
                ScopusAverage = ScopusAverage.round(0)

       else:
           ScopusAverage = "Not selected"

       if CochraneLibraryDatabase=="on":
           CochraneLibraryAverage = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')['Cochrane Library'].mean()
           if pd.isna(CochraneLibraryAverage):
                CochraneLibraryAverage = "No data"
           else:
                CochraneLibraryAverage = CochraneLibraryAverage.round(0)

       else:
           CochraneLibraryAverage = "Not selected"

       if CochraneCentralDatabase=="on":
           CochraneCentralAverage = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')['Cochrane Central'].mean()
           if pd.isna(CochraneCentralAverage):
                CochraneCentralAverage = "No data"
           else:
                CochraneCentralAverage = CochraneCentralAverage.round(0)

       else:
           CochraneCentralAverage = "Not selected"

       if ERICDatabase=="on":
           ERICAverage = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')['ERIC'].mean()
           if pd.isna(ERICAverage):
                ERICAverage = "No data"
           else:
                ERICAverage = ERICAverage.round(0)

       else:
           ERICAverage = "Not selected"

       if PEDroDatabase=="on":
           PEDroAverage = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')['PEDro'].mean()
           if pd.isna(PEDroAverage):
                PEDroAverage = "No data"
           else:
                PEDroAverage = PEDroAverage.round(0)

       else:
           PEDroAverage = "Not selected"

       if PsycINFODatabase=="on":
           PsycINFOAverage = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')['PsycINFO'].mean()
           if pd.isna(PsycINFOAverage):
                PsycINFOAverage = "No data"
           else:
                PsycINFOAverage = PsycINFOAverage.round(0)

       else:
           PsycINFOAverage = "Not selected"

       if WebOfScienceDatabase=="on":
           WebOfScienceAverage = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')['Web of Science'].mean()
           if pd.isna(WebOfScienceAverage):
                WebOfScienceAverage = "No data"
           else:
                WebOfScienceAverage = WebOfScienceAverage.round(0)

       else:
           WebOfScienceAverage = "Not selected"
  
       UniqueAverage = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')['Unique'].mean()
       if pd.isna(UniqueAverage):
           UniqueAverage = "No data"
       else:
           UniqueAverage = UniqueAverage.round(0)    

       
       IncludesAverage = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')['Includes'].mean()
       if pd.isna(IncludesAverage):
           IncludesAverage = "No data"
       else:
           IncludesAverage = IncludesAverage.round(0) 

       GreyLiteratureAverage = df.query('Medline - @TotalMedline <= 99 & Medline - @TotalMedline > -99 & Topics == @Topics')['Grey Literature'].mean()
       if pd.isna(GreyLiteratureAverage):
           GreyLiteratureAverage = "No data"
       else:
           GreyLiteratureAverage = GreyLiteratureAverage.round(0) 
             
       TotalScreen = ([TotalMedline, CINAHLAverage, CochraneLibraryAverage, CochraneCentralAverage, ERICAverage, PEDroAverage, PsycINFOAverage, EmbaseAverage, ScopusAverage, WebOfScienceAverage, GreyLiteratureAverage, DatabaseSelection1Records, DatabaseSelection2Records, DatabaseSelection3Records, DatabaseSelection4Records, DatabaseSelection5Records, DatabaseSelection6Records, DatabaseSelection7Records, DatabaseSelection8Records, DatabaseSelection9Records, DatabaseSelection10Records])
       TotalScreen = sum(x if not isinstance(x,str) else 0 for x in TotalScreen)
           
       if TotalScreen==0:
           TotalScreen="No results"
       elif TotalScreen==TotalMedline:
           TotalScreen="No results"         
    else:
        CINAHLAverage = ""
        EmbaseAverage = ""
        ScopusAverage = ""
        CochraneLibraryAverage = ""
        CochraneCentralAverage = ""
        ERICAverage = ""
        PEDroAverage = ""
        PsycINFOAverage = ""
        WebOfScienceAverage = ""
        IncludesAverage = ""
        UniqueAverage = ""
        TotalScreen = ""
        TotalMedline = ""
        GreyLiteratureAverage = ""
        display1 = "display: none"
        display2 = "display: none"
        display3 = "display: none"
        display4 = "display: none"
        display5 = "display: none"
        display6 = "display: none"
        display7 = "display: none"
        display8 = "display: none"
        display9 = "display: none"
        display10 = "display: none"
        DatabaseSelection1 = ""
        DatabaseSelection1Records = ""
        DatabaseSelection2 = ""
        DatabaseSelection2Records = ""
        DatabaseSelection3 = ""
        DatabaseSelection3Records = ""
        DatabaseSelection4 = ""
        DatabaseSelection4Records = ""
        DatabaseSelection5 = ""
        DatabaseSelection5Records = ""
        DatabaseSelection6 = ""
        DatabaseSelection6Records = ""
        DatabaseSelection7 = ""
        DatabaseSelection7Records = ""
        DatabaseSelection8 = ""
        DatabaseSelection8Records = ""
        DatabaseSelection9 = ""
        DatabaseSelection9Records = ""
        DatabaseSelection10 = ""
        DatabaseSelection10Records = ""
        AlliedDisplay = "display: none"
        MedicineDisplay = "display: none"

    return render_template("form.html",CINAHLRecords = CINAHLAverage, CochraneLibraryRecords = CochraneLibraryAverage, CochraneCentralRecords = CochraneCentralAverage, ERICRecords = ERICAverage, PEDroRecords = PEDroAverage, PsycINFORecords = PsycINFOAverage, WebOfScienceRecords = WebOfScienceAverage, EmbaseRecords = EmbaseAverage, ScopusRecords = ScopusAverage, IncludesRecords = IncludesAverage, UniqueRecords = UniqueAverage, TotalScreen=TotalScreen, MedlineRecords=TotalMedline, GreyLiteratureRecords=GreyLiteratureAverage, display1 = display1, display2 = display2, display3 = display3, display4 = display4, display5 = display5, display6 = display6, display7 = display7, display8 = display8, display9 = display9, display10 = display10, DatabaseSelection1Name = DatabaseSelection1, DatabaseSelection1Records = DatabaseSelection1Records, DatabaseSelection2Name = DatabaseSelection2, DatabaseSelection2Records = DatabaseSelection2Records, DatabaseSelection3Name = DatabaseSelection3, DatabaseSelection3Records = DatabaseSelection3Records, DatabaseSelection4Name = DatabaseSelection4, DatabaseSelection4Records = DatabaseSelection4Records, DatabaseSelection5Name = DatabaseSelection5, DatabaseSelection5Records = DatabaseSelection5Records, DatabaseSelection6Name = DatabaseSelection6, DatabaseSelection6Records = DatabaseSelection6Records, DatabaseSelection7Name = DatabaseSelection7, DatabaseSelection7Records = DatabaseSelection7Records, DatabaseSelection8Name = DatabaseSelection8, DatabaseSelection8Records = DatabaseSelection8Records, DatabaseSelection9Name = DatabaseSelection9, DatabaseSelection9Records = DatabaseSelection9Records, DatabaseSelection10Name = DatabaseSelection10, DatabaseSelection10Records = DatabaseSelection10Records, MedicineDisplay = MedicineDisplay, AlliedDisplay = AlliedDisplay)

if __name__=='__main__':
   app.run()