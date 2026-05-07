from flask import Flask, request, render_template
import pandas as pd
from pathlib import Path

app = Flask(__name__)  

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
       ForensicTopic = request.form.get("ForensicTopic")
       HealthInformaticsTopic = request.form.get("HealthInformaticsTopic")
       LawEthicsTopic = request.form.get("LawEthicsTopic")
       LibraryScienceTopic = request.form.get("LibraryScienceTopic")
       MedicineTopic = request.form.get("MedicineTopic")
       NursingTopic = request.form.get("NursingTopic")
       PharmacyTopic = request.form.get("PharmacyTopic")
       PhysicalTopic = request.form.get("PhysicalTopic")
       PoliticalTopic = request.form.get("PoliticalTopic")
       PsychologyTopic = request.form.get("PsychologyTopic")
       ResearchTopic = request.form.get("ResearchTopic")
       SociologyTopic = request.form.get("SociologyTopic")
       SportsTopic = request.form.get("SportsTopic")
       ToxicologyTopic = request.form.get("ToxicologyTopic")
       UrbanTopic = request.form.get("UrbanTopic")
       VeterinaryTopic = request.form.get("VeterinaryTopic")
       
       ArtTopic = request.form.get("ArtTopic")
       AudiologyTopic = request.form.get("AudiologyTopic")
       CaregivingTopic = request.form.get("CaregivingTopic") 
       ChiropracticTopic = request.form.get("ChiropracticTopic") 
       DieteticsTopic = request.form.get("DieteticsTopic") 
       ImagingTopic = request.form.get("ImagingTopic") 
       InfectionPreventionTopic = request.form.get("InfectionPreventionTopic") 
       MidwiferyTopic = request.form.get("MidwiferyTopic") 
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
       CriticalTopic = request.form.get("CriticalTopic")
       EarTopic = request.form.get("EarTopic")
       EmergencyTopic = request.form.get("EmergencyTopic")
       EyeTopic = request.form.get("EyeTopic")
       GeriatricsTopic = request.form.get("GeriatricsTopic")
       InfectionTopic = request.form.get("InfectionTopic")
       InflammatoryTopic = request.form.get("InflammatoryTopic")
       InjuriesTopic = request.form.get("InjuriesTopic")
       MetabolicTopic = request.form.get("MetabolicTopic")
       MusculoskeletalTopic = request.form.get("MusculoskeletalTopic")
       NeurologicalTopic = request.form.get("NeurologicalTopic")
       OccupationalMedTopic = request.form.get("OccupationalMedTopic")
       OralTopic = request.form.get("OralTopic")
       PalliativeTopic = request.form.get("PalliativeTopic")
       PathologyTopic = request.form.get("PathologyTopic")
       PediatricsTopic = request.form.get("PediatricsTopic")
       RenalTopic = request.form.get("RenalTopic")
       ReproductiveTopic = request.form.get("ReproductiveTopic")
       RespiratoryTopic = request.form.get("RespiratoryTopic")
       SkinTopic = request.form.get("SkinTopic")
       SleepTopic = request.form.get("SleepTopic")
       SpaceTopic = request.form.get("SpaceTopic")
       StrokeTopic = request.form.get("StrokeTopic")
       SurgeryTopic = request.form.get("SurgeryTopic")
       TelemedicineTopic = request.form.get("TelemedicineTopic")
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

       Algorithmic = request.form.get("Algorithmic")
       AuthorSearch = request.form.get("AuthorSearch")
       Citations = request.form.get("Citations")
       Discovery = request.form.get("Discovery")
       GeneralGrey = request.form.get("GeneralGrey")
       GeneralWeb = request.form.get("GeneralWeb")
       Guidelines = request.form.get("Guidelines")
       Hand = request.form.get("Hand")
       HealthTechnology = request.form.get("HealthTechnology")
       Institutional = request.form.get("Institutional")
       National = request.form.get("National")
       PersonalCommunication = request.form.get("PersonalCommunication")
       Preprints = request.form.get("Preprints")
       PointOfCare = request.form.get("PointOfCare")
       PreviousReviews = request.form.get("PreviousReviews")
       PriorKnowledge = request.form.get("PriorKnowledge")
       Protocols = request.form.get("Protocols")
       Scholarly = request.form.get("Scholarly")
       SubjectSearch = request.form.get("SubjectSearch")
       Theses = request.form.get("Theses")
       TrialRegistries = request.form.get("TrialRegistries")
       UpdatesAlerts= request.form.get("UpdatesAlerts")
       UnknownUnclear = request.form.get("UnknownUnclear")
        
       Topics = []
       GreyLiteratureSelection = []
       DatabaseList = []
       TotalMedline = float(TotalMedline) 

       if AgricultureTopic=="on":
           Topics.append("Agriculture")
           AgricultureChecked = "checked"
       else:
           AgricultureChecked = ""
       if AlliedTopic=="on":
           Topics.append("Allied Health")
           AlliedDisplay = ""
           AlliedChecked = "checked"
           AlliedDisabled = ""
       else:
           AlliedDisplay = "display: none;"
           AlliedChecked = ""
           AlliedDisabled = "disabled='disabled'"
       if BiochemistryTopic=="on":
           Topics.append("Biochemistry, Genetics, and Microbiology")
           BiochemistryChecked = "checked"
       else:
           BiochemistryChecked = ""
       if BusinessTopic=="on":
           Topics.append("Business and Economics")
           BusinessChecked = "checked"
       else:
           BusinessChecked = ""
       if DentistryTopic=="on":
           Topics.append("Dentistry")
           DentistryChecked = "checked"
       else:
           DentistryChecked = ""
       if DrugsTopic=="on":
           Topics.append("Drugs and Supplements (not toxicology)")    
           DrugsChecked = "checked"
       else:
           DrugsChecked = ""
       if EcologyTopic=="on":
           Topics.append("Ecology and Zoology")
           EcologyChecked = "checked"
       else:
           EcologyChecked = ""
       if EducationTopic=="on":
           Topics.append("Education")
           EducationChecked = "checked"
       else:
           EducationChecked = ""
       if EngineeringTopic=="on":
           Topics.append("Engineering")
           EngineeringChecked = "checked"
       else:
           EngineeringChecked = ""
       if EnvironmentalTopic=="on":
           Topics.append("Environmental Science")
           EnvironmentalChecked = "checked"
       else:
           EnvironmentalChecked = ""

       if ForensicTopic=="on":
           Topics.append("Forensic Science")
           ForensicChecked = "checked"
       else:
           ForensicChecked = ""

       if HealthInformaticsTopic=="on":
           Topics.append("Health Informatics")
           HealthInformaticsChecked = "checked"
       else:
           HealthInformaticsChecked = ""

       if LawEthicsTopic=="on":
           Topics.append("Law and Ethics")
           LawEthicsChecked = "checked"
       else:
           LawEthicsChecked = ""

       if LibraryScienceTopic=="on":
           Topics.append("Library and Information Science")
           LibraryScienceChecked = "checked"
       else:
           LibraryScienceChecked = ""

        
       if MedicineTopic=="on":
           Topics.append("Medicine")
           MedicineDisplay = ""
           MedicineChecked = "checked"
           MedicineDisabled = ""
       else:
           MedicineDisplay = "display: none;"
           MedicineChecked = ""
           MedicineDisabled = "disabled='disabled'"
       if NursingTopic=="on":
           Topics.append("Nursing")
           NursingChecked = "checked"
       else:
           NursingChecked = ""

       if PharmacyTopic=="on":
           Topics.append("Pharmacy")
           PharmacyChecked = "checked"
       else:
           PharmacyChecked = ""
        
       if PhysicalTopic=="on":
           Topics.append("Physical Sciences and Mathematics")
           PhysicalChecked = "checked"
       else:
           PhysicalChecked = ""

       if PoliticalTopic=="on":
           Topics.append("Political Science")
           PoliticalChecked = "checked"
       else:
           PoliticalChecked = ""
        
       if PsychologyTopic=="on":
           Topics.append("Psychology, Psychiatry and Mental Health")
           PsychologyChecked = "checked"
       else:
           PsychologyChecked = ""

       if ResearchTopic=="on":
           Topics.append("Research Methods")
           ResearchChecked = "checked"
       else:
           ResearchChecked = ""

       if SociologyTopic=="on":
           Topics.append("Sociology")
           SociologyChecked = "checked"
       else:
           SociologyChecked = ""
        
       if SportsTopic=="on":
           Topics.append("Sports and Recreation")
           SportsChecked = "checked"
       else:
           SportsChecked = ""

       if ToxicologyTopic=="on":
           Topics.append("Toxicology")
           ToxicologyChecked = "checked"
       else:
           ToxicologyChecked = ""

       if UrbanTopic=="on":
           Topics.append("Urban Planning")
           UrbanChecked = "checked"
       else:
           UrbanChecked = ""
        
       if VeterinaryTopic=="on":
           Topics.append("Veterinary")
           VeterinaryChecked = "checked"
       else:
           VeterinaryChecked = ""

       if BloodTopic=="on":
           Topics.append("Blood and hematology")
           BloodChecked = "checked"
       else:
           BloodChecked = ""
       if CancerTopic=="on":
           Topics.append("Cancer")
           CancerChecked = "checked"
       else:
           CancerChecked = ""
       if CardiovascularTopic=="on":
           Topics.append("Cardiovascular")
           CardiovascularChecked = "checked"
       else:
           CardiovascularChecked = ""
       if ComplementaryTopic=="on":
           Topics.append("Complementary and alternative medicine")
           ComplementaryChecked = "checked"
       else:
           ComplementaryChecked = ""
       if CongenitalTopic=="on":
           Topics.append("Congenital disorders")
           CongenitalChecked = "checked"
       else:
           CongenitalChecked = ""

       if CriticalTopic=="on":
           Topics.append("Critical care medicine")
           CriticalChecked = "checked"
       else:
           CriticalChecked = ""
        
       if EarTopic=="on":
           Topics.append("Ear and hearing")
           EarChecked = "checked"
       else:
           EarChecked = ""

       if EmergencyTopic=="on":
           Topics.append("Emergency medicine")
           EmergencyChecked = "checked"
       else:
           EmergencyChecked = ""

       if EyeTopic=="on":
           Topics.append("Eye and vision")
           EyeChecked = "checked"
       else:
           EyeChecked = ""
       if GeriatricsTopic=="on":
           Topics.append("Geriatrics and gerontology")
           GeriatricsChecked = "checked"
       else:
           GeriatricsChecked = ""
       if InfectionTopic=="on":
           Topics.append("Infection")
           InfectionChecked = "checked"
       else:
           InfectionChecked = ""
       if InflammatoryTopic=="on":
           Topics.append("Inflammatory and immune system")
           InflammatoryChecked = "checked"
       else:
           InflammatoryChecked = ""
       if InjuriesTopic=="on":
           Topics.append("Injuries and accidents")
           InjuriesChecked = "checked"
       else:
           InjuriesChecked = ""
       if MetabolicTopic=="on":
           Topics.append("Metabolic and endocrine")
           MetabolicChecked = "checked"
       else:
           MetabolicChecked = ""
       if MusculoskeletalTopic=="on":
           Topics.append("Musculoskeletal")
           MusculoskeletalChecked = "checked"
       else:
           MusculoskeletalChecked = ""
       if NeurologicalTopic=="on":
           Topics.append("Neurological")
           NeurologicalChecked = "checked"
       else:
           NeurologicalChecked = ""

       if OccupationalMedTopic=="on":
           Topics.append("Occupational medicine")
           OccupationalMedChecked = "checked"
       else:
           OccupationalMedChecked = ""
        
       if OralTopic=="on":
           Topics.append("Oral and gastrointestinal")
           OralChecked = "checked"
       else:
           OralChecked = ""

       if PalliativeTopic=="on":
           Topics.append("Palliative medicine")
           PalliativeChecked = "checked"
       else:
           PalliativeChecked = ""

       if PathologyTopic=="on":
           Topics.append("Pathology and forensic medicine")
           PathologyChecked = "checked"
       else:
           PathologyChecked = ""
        
       if PediatricsTopic=="on":
           Topics.append("Pediatrics and neonatology")
           PediatricsChecked = "checked"
       else:
           PediatricsChecked = ""
       if RenalTopic=="on":
           Topics.append("Renal, gynecological and urogenital")
           RenalChecked = "checked"
       else:
           RenalChecked = ""
       if ReproductiveTopic=="on":
           Topics.append("Reproductive health and childbirth")
           ReproductiveChecked = "checked"
       else:
           ReproductiveChecked = ""
       if RespiratoryTopic=="on":
           Topics.append("Respiratory")
           RespiratoryChecked = "checked"
       else:
           RespiratoryChecked = ""
       if SkinTopic=="on":
           Topics.append("Skin")
           SkinChecked = "checked"
       else:
           SkinChecked = ""
       if SleepTopic=="on":
           Topics.append("Sleep")
           SleepChecked = "checked"
       else:
           SleepChecked = ""

       if SpaceTopic=="on":
           Topics.append("Space medicine")
           SpaceChecked = "checked"
       else:
           SpaceChecked = ""
        
       if StrokeTopic=="on":
           Topics.append("Stroke")
           StrokeChecked = "checked"
       else:
           StrokeChecked = ""
       if SurgeryTopic=="on":
           Topics.append("Surgery")
           SurgeryChecked = "checked"
       else:
           SurgeryChecked = ""

       if TelemedicineTopic=="on":
           Topics.append("Telemedicine")
           TelemedicineChecked = "checked"
       else:
           TelemedicineChecked = ""
        
       if GeneralTopic=="on":
           Topics.append("General and public health and safety")
           GeneralChecked = "checked"
       else:
           GeneralChecked = ""

       if ArtTopic=="on":
           Topics.append("Art/music/drama therapy")
           ArtChecked = "checked"
       else:
           ArtChecked = ""
       if AudiologyTopic=="on":
           Topics.append("Audiology and speech-language pathology")
           AudiologyChecked = "checked"
       else:
           AudiologyChecked = ""

       if CaregivingTopic=="on":
           Topics.append("Caregiving")
           CaregivingChecked = "checked"
       else:
           CaregivingChecked = ""

       if ChiropracticTopic=="on":
           Topics.append("Chiropractic")
           ChiropracticChecked = "checked"
       else:
           ChiropracticChecked = ""

       if DieteticsTopic=="on":
           Topics.append("Dietetics")
           DieteticsChecked = "checked"
       else:
           DieteticsChecked = ""
       if ImagingTopic=="on":
           Topics.append("Imaging")
           ImagingChecked = "checked"
       else:
           ImagingChecked = ""

       if InfectionPreventionTopic=="on":
           Topics.append("Infection prevention and control")
           InfectionPreventionChecked = "checked"
       else:
           InfectionPreventionChecked = ""

       if MidwiferyTopic=="on":
           Topics.append("Midwifery")
           MidwiferyChecked = "checked"
       else:
           MidwiferyChecked = ""
    
       if OccupationalTopic=="on":
           Topics.append("Occupational therapy")
           OccupationalChecked = "checked"
       else:
           OccupationalChecked = ""
       if PhysiotherapyTopic=="on":
           Topics.append("Physiotherapy")
           PhysiotherapyChecked = "checked"
       else:
           PhysiotherapyChecked = ""
       if PrehospitalTopic=="on":
           Topics.append("Prehospital care")
           PrehospitalChecked = "checked"
       else:
           PrehospitalChecked = ""
       if ProstheticsTopic=="on":
           Topics.append("Prosthetics and orthotics")
           ProstheticsChecked = "checked"
       else:
           ProstheticsChecked = ""
       if RecreationTopic=="on":
           Topics.append("Recreation therapy")
           RecreationChecked = "checked"
       else:
           RecreationChecked = ""
       if RespiratoryTherapyTopic=="on":
           Topics.append("Respiratory therapy")
           RespiratoryTherapyChecked = "checked"
       else:
           RespiratoryTherapyChecked = ""
       if SocialTopic=="on":
           Topics.append("Social work")
           SocialChecked = "checked"
       else:
           SocialChecked = ""
       if SpiritualTopic=="on":
           Topics.append("Spiritual care")
           SpiritualChecked = "checked"
       else:
           SpiritualChecked = ""

       if Algorithmic=="on":
           GreyLiteratureSelection.append("Algorithmic and visualization tools")
           AlgorithmicChecked = "checked"
       else:
           AlgorithmicChecked = ""

       if AuthorSearch=="on":
           GreyLiteratureSelection.append("Author search")
           AuthorSearchChecked = "checked"
       else:
           AuthorSearchChecked = ""

       if Citations=="on":
           GreyLiteratureSelection.append("Citation searching")
           CitationsChecked = "checked"
       else:
           CitationsChecked = ""

       if Discovery=="on":
           GreyLiteratureSelection.append("Discovery tools and union catalogues")
           DiscoveryChecked = "checked"
       else:
           DiscoveryChecked = ""

       if GeneralGrey=="on":
           GreyLiteratureSelection.append("General grey literature search tools")
           GeneralGreyChecked = "checked"
       else:
           GeneralGreyChecked = ""

       if GeneralWeb=="on":
           GreyLiteratureSelection.append("General web searches")
           GeneralWebChecked = "checked"
       else:
           GeneralWebChecked = ""

       if Guidelines=="on":
           GreyLiteratureSelection.append("Guidelines")
           GuidelinesChecked = "checked"
       else:
           GuidelinesChecked = ""

       if Hand=="on":
           GreyLiteratureSelection.append("Hand searching")
           HandChecked = "checked"
       else:
           HandChecked = ""

       if HealthTechnology=="on":
           GreyLiteratureSelection.append("Health technology assessments")
           HealthTechnologyChecked = "checked"
       else:
           HealthTechnologyChecked = ""

       if Institutional=="on":
           GreyLiteratureSelection.append("Institutional repositories")
           InstitutionalChecked = "checked"
       else:
           InstitutionalChecked = ""

       if National=="on":
           GreyLiteratureSelection.append("National repositories")
           NationalChecked = "checked"
       else:
           NationalChecked = ""

       if PersonalCommunication=="on":
           GreyLiteratureSelection.append("Personal communication")
           PersonalCommunicationChecked = "checked"
       else:
           PersonalCommunicationChecked = ""

       if Preprints=="on":
           GreyLiteratureSelection.append("Preprints")
           PreprintsChecked = "checked"
       else:
           PreprintsChecked = ""

       if PointOfCare=="on":
           GreyLiteratureSelection.append("Point of care")
           PointOfCareChecked = "checked"
       else:
           PointOfCareChecked = ""

       if PreviousReviews=="on":
           GreyLiteratureSelection.append("Previous reviews")
           PreviousReviewsChecked = "checked"
       else:
           PreviousReviewsChecked = ""

       if PriorKnowledge=="on":
           GreyLiteratureSelection.append("Prior knowledge")
           PriorKnowledgeChecked = "checked"
       else:
           PriorKnowledgeChecked = ""

       if Protocols=="on":
           GreyLiteratureSelection.append("Protocols")
           ProtocolsChecked = "checked"
       else:
           ProtocolsChecked = ""

       if Scholarly=="on":
           GreyLiteratureSelection.append("Scholarly search engines")
           ScholarlyChecked = "checked"
       else:
           ScholarlyChecked = ""

       if SubjectSearch=="on":
           GreyLiteratureSelection.append("Subject repositories and search tools")
           SubjectSearchedChecked = "checked"
       else:
           SubjectSearchedChecked = ""

       if Theses=="on":
           GreyLiteratureSelection.append("Theses or dissertations")
           ThesesChecked = "checked"
       else:
           ThesesChecked = ""

       if TrialRegistries=="on":
           GreyLiteratureSelection.append("Trial registries")
           TrialRegistriesChecked = "checked"
       else:
           TrialRegistriesChecked = ""

       if UnknownUnclear=="on":
           GreyLiteratureSelection.append("Unknown/unclear")
           UnknownUnclearChecked = "checked"
       else:
           UnknownUnclearChecked = ""

       if UpdatesAlerts=="on":
           GreyLiteratureSelection.append("Updates or alerts")
           UpdatesAlertsChecked = "checked"
       else:
           UpdatesAlertsChecked = ""

       GreyLiteratureSelection = sorted(GreyLiteratureSelection)

        
       for idx, val in enumerate(Topics):
           globals()[f'Topic_{idx}'] = val

       pd.options.display.float_format = '{:.0f}'.format
       CSV_FILE_PATH = Path.cwd() / 'SR Calculator Github.csv'
       df = pd.read_csv(CSV_FILE_PATH, dtype={'UniquePercentNoGrey': 'float64','UniquePercent': 'float64', 'DatabaseIncludesPercent':'float64','GreyLiteratureIncludesPercent':'float64'})
       df.head()

       if 'Topic_10' in globals():
           Topicdf = df.query('Topics.str.contains(@Topic_0) & Topics.str.contains(@Topic_1) & Topics.str.contains(@Topic_2) & Topics.str.contains(@Topic_3) & Topics.str.contains(@Topic_4) & Topics.str.contains(@Topic_5) & Topics.str.contains(@Topic_6) & Topics.str.contains(@Topic_7) & Topics.str.contains(@Topic_8) & Topics.str.contains(@Topic_9) & Topics.str.contains(@Topic_10)')      

       elif 'Topic_9' in globals(): 
           Topicdf = df.query('Topics.str.contains(@Topic_0) & Topics.str.contains(@Topic_1) & Topics.str.contains(@Topic_2) & Topics.str.contains(@Topic_3) & Topics.str.contains(@Topic_4) & Topics.str.contains(@Topic_5) & Topics.str.contains(@Topic_6) & Topics.str.contains(@Topic_7) & Topics.str.contains(@Topic_8) & Topics.str.contains(@Topic_9)')      
    
       elif 'Topic_8' in globals(): 
           Topicdf = df.query('Topics.str.contains(@Topic_0) & Topics.str.contains(@Topic_1) & Topics.str.contains(@Topic_2) & Topics.str.contains(@Topic_3) & Topics.str.contains(@Topic_4) & Topics.str.contains(@Topic_5) & Topics.str.contains(@Topic_6) & Topics.str.contains(@Topic_7) & Topics.str.contains(@Topic_8)')      
        
       elif 'Topic_7' in globals(): 
           Topicdf = df.query('Topics.str.contains(@Topic_0) & Topics.str.contains(@Topic_1) & Topics.str.contains(@Topic_2) & Topics.str.contains(@Topic_3) & Topics.str.contains(@Topic_4) & Topics.str.contains(@Topic_5) & Topics.str.contains(@Topic_6) & Topics.str.contains(@Topic_7)')      
        
       elif 'Topic_6' in globals(): 
           Topicdf = df.query('Topics.str.contains(@Topic_0) & Topics.str.contains(@Topic_1) & Topics.str.contains(@Topic_2) & Topics.str.contains(@Topic_3) & Topics.str.contains(@Topic_4) & Topics.str.contains(@Topic_5) & Topics.str.contains(@Topic_6)')      
        
       elif 'Topic_5' in globals(): 
           Topicdf = df.query('Topics.str.contains(@Topic_0) & Topics.str.contains(@Topic_1) & Topics.str.contains(@Topic_2) & Topics.str.contains(@Topic_3) & Topics.str.contains(@Topic_4) & Topics.str.contains(@Topic_5)')      
     
       elif 'Topic_4' in globals(): 
           Topicdf = df.query('Topics.str.contains(@Topic_0) & Topics.str.contains(@Topic_1) & Topics.str.contains(@Topic_2) & Topics.str.contains(@Topic_3) & Topics.str.contains(@Topic_4)')      
        
       elif 'Topic_3' in globals(): 
           Topicdf = df.query('Topics.str.contains(@Topic_0) & Topics.str.contains(@Topic_1) & Topics.str.contains(@Topic_2) & Topics.str.contains(@Topic_3)')      
        
       elif 'Topic_2' in globals(): 
           Topicdf = df.query('Topics.str.contains(@Topic_0) & Topics.str.contains(@Topic_1) & Topics.str.contains(@Topic_2)')      
        
       elif 'Topic_1' in globals(): 
           Topicdf = df.query('Topics.str.contains(@Topic_0) & Topics.str.contains(@Topic_1)')      
        
       elif 'Topic_0' in globals(): 
           Topicdf = df.query('Topics.str.contains(@Topic_0)')      
              
       Medlinedf = Topicdf.query('MedlineAverage - @TotalMedline <= 99 & MedlineAverage - @TotalMedline > -99')
        
       if CINAHLDatabase=="on":
           CINAHLChecked = "checked"
           CINAHLAverage = Medlinedf['CINAHL'].mean(numeric_only=True)
           DatabaseList.append('CINAHL')
           if pd.isna(CINAHLAverage):
                CINAHLAverage = "No data"
           else:
                CINAHLAverage = CINAHLAverage.round(0).astype(int)

       else:
           CINAHLAverage = ""
           CINAHLChecked = ""

       if CochraneLibraryDatabase=="on":
           CochraneLibraryChecked = "checked"
           CochraneLibraryAverage = Medlinedf['Cochrane Library'].mean(numeric_only=True)
           DatabaseList.append('Cochrane Library')
           if pd.isna(CochraneLibraryAverage):
                CochraneLibraryAverage = "No data"
           else:
                CochraneLibraryAverage = CochraneLibraryAverage.round(0).astype(int)

       else:
           CochraneLibraryChecked = ""
           CochraneLibraryAverage = ""

       if CochraneCentralDatabase=="on":
           CochraneCentralChecked = "checked"
           CochraneCentralAverage = Medlinedf['Cochrane Central'].mean(numeric_only=True)
           DatabaseList.append('Cochrane Central')
           if pd.isna(CochraneCentralAverage):
                CochraneCentralAverage = "No data"
           else:
                CochraneCentralAverage = CochraneCentralAverage.round(0).astype(int)

       else:
           CochraneCentralChecked = ""
           CochraneCentralAverage = ""        
      
       if EmbaseDatabase=="on":
           EmbaseChecked = "checked"
           EmbaseAverage = Medlinedf['Embase'].mean(numeric_only=True)
           DatabaseList.append('Embase')
           if pd.isna(EmbaseAverage):
                EmbaseAverage = "No data"
           else:
                EmbaseAverage = EmbaseAverage.round(0).astype(int)

       else:
           EmbaseAverage = ""
           EmbaseChecked = ""

       if ERICDatabase=="on":
           ERICChecked = "checked"
           ERICAverage = Medlinedf['ERIC'].mean(numeric_only=True)
           DatabaseList.append('ERIC')
           if pd.isna(ERICAverage):
                ERICAverage = "No data"
           else:
                ERICAverage = ERICAverage.round(0).astype(int)

       else:
           ERICChecked = ""
           ERICAverage = ""

       if PEDroDatabase=="on":
           PEDroChecked = "checked"
           PEDroAverage = Medlinedf['PEDro'].mean(numeric_only=True)
           DatabaseList.append('PEDro')
           if pd.isna(PEDroAverage):
                PEDroAverage = "No data"
           else:
                PEDroAverage = PEDroAverage.round(0).astype(int)

       else:
           PEDroChecked = ""
           PEDroAverage = ""


       if PsycINFODatabase=="on":
           PsycINFOChecked = "checked"
           PsycINFOAverage = Medlinedf['PsycINFO'].mean(numeric_only=True)
           DatabaseList.append('PsycINFO')
           if pd.isna(PsycINFOAverage):
                PsycINFOAverage = "No data"
           else:
                PsycINFOAverage = PsycINFOAverage.round(0).astype(int)

       else:
           PsycINFOChecked = ""
           PsycINFOAverage = ""
        
       if ScopusDatabase=="on":
           ScopusChecked = "checked"
           ScopusAverage = Medlinedf['Scopus'].mean(numeric_only=True)
           DatabaseList.append('Scopus')
           if pd.isna(ScopusAverage):
                ScopusAverage = "No data"
           else:
                ScopusAverage = ScopusAverage.round(0).astype(int)

       else:
           ScopusAverage = ""
           ScopusChecked = ""


       if WebOfScienceDatabase=="on":
           WebOfScienceChecked = "checked"
           WebOfScienceAverage = Medlinedf['Web of Science'].mean(numeric_only=True)
           DatabaseList.append('Web of Science')
           if pd.isna(WebOfScienceAverage):
                WebOfScienceAverage = "No data"
           else:
                WebOfScienceAverage = WebOfScienceAverage.round(0).astype(int)

       else:
           WebOfScienceChecked = ""
           WebOfScienceAverage = ""

       if DatabaseSelection1=="selectone":
           display1 = "display: none;"
           DatabaseSelection1 = ""
           DatabaseSelection1Records = ""
       elif DatabaseSelection1==None:
           display1 = "display: none;"
           DatabaseSelection1 = ""
           DatabaseSelection1Records = ""
       else:
           display1 = ""
           DatabaseSelection1Average = Medlinedf[DatabaseSelection1].mean(numeric_only=True)
           if pd.isna(DatabaseSelection1Average):
                DatabaseSelection1Records = "No data"
           else:
                DatabaseSelection1Records = DatabaseSelection1Average.round(0).astype(int)

       if DatabaseSelection2=="selectone":
           display2 = "display: none;"
           DatabaseSelection2 = ""
           DatabaseSelection2Records = ""
       elif DatabaseSelection2==None:
           display2 = "display: none;"
           DatabaseSelection2 = ""
           DatabaseSelection2Records = ""
       else:
           display2 = ""
           DatabaseSelection2Average = Medlinedf[DatabaseSelection2].mean(numeric_only=True)
           if pd.isna(DatabaseSelection2Average):
                DatabaseSelection2Records = "No data"
           else:
                DatabaseSelection2Records = DatabaseSelection2Average.round(0).astype(int)

       if DatabaseSelection3=="selectone":
           display3 = "display: none;"
           DatabaseSelection = ""
           DatabaseSelection3Records = ""
       elif DatabaseSelection3==None:
           display3 = "display: none;"
           DatabaseSelection3 = ""
           DatabaseSelection3Records = ""
       else:
           display3 = ""
           DatabaseSelection3Average = Medlinedf[DatabaseSelection3].mean(numeric_only=True)
           if pd.isna(DatabaseSelection3Average):
                DatabaseSelection3Records = "No data"
           else:
                DatabaseSelection3Records = DatabaseSelection3Average.round(0).astype(int)      

       if DatabaseSelection4=="selectone":
           display4 = "display: none;"
           DatabaseSelection4 = ""
           DatabaseSelection4Records = ""
       elif DatabaseSelection4==None:
           display4 = "display: none;"
           DatabaseSelection4 = ""
           DatabaseSelection4Records = ""
       else:
           display4 = ""
           DatabaseSelection4Average = Medlinedf[DatabaseSelection4].mean(numeric_only=True)
           if pd.isna(DatabaseSelection4Average):
                DatabaseSelection4Records = "No data"
           else:
                DatabaseSelection4Records = DatabaseSelection4Average.round(0).astype(int)
 
       if DatabaseSelection5=="selectone":
           display5 = "display: none;"
           DatabaseSelection5 = ""
           DatabaseSelection5Records = ""
       elif DatabaseSelection5==None:
           display5 = "display: none;"
           DatabaseSelection5 = ""
           DatabaseSelection5Records = ""
       else:
           display5 = ""
           DatabaseSelection5Average = Medlinedf[DatabaseSelection5].mean(numeric_only=True)
           if pd.isna(DatabaseSelection5Average):
                DatabaseSelection5Records = "No data"
           else:
                DatabaseSelection5Records = DatabaseSelection5Average.round(0).astype(int)
 
       if DatabaseSelection6=="selectone":
           display6 = "display: none;"
           DatabaseSelection6 = ""
           DatabaseSelection6Records = ""
       elif DatabaseSelection6==None:
           display6 = "display: none;"
           DatabaseSelection6 = ""
           DatabaseSelection6Records = ""
       else:
           display6 = ""
           DatabaseSelection6Average = Medlinedf[DatabaseSelection6].mean(numeric_only=True)
           if pd.isna(DatabaseSelection6Average):
                DatabaseSelection6Records = "No data"
           else:
                DatabaseSelection6Records = DatabaseSelection6Average.round(0).astype(int)
 
       if DatabaseSelection7=="selectone":
           display7 = "display: none;"
           DatabaseSelection7 = ""
           DatabaseSelection7Records = ""
       elif DatabaseSelection7==None:
           display7 = "display: none;"
           DatabaseSelection7 = ""
           DatabaseSelection7Records = ""
       else:
           display7 = ""
           DatabaseSelection7Average = Medlinedf[DatabaseSelection7].mean(numeric_only=True)
           if pd.isna(DatabaseSelection7Average):
                DatabaseSelection7Records = "No data"
           else:
                DatabaseSelection7Records = DatabaseSelection7Average.round(0).astype(int)
 
       if DatabaseSelection8=="selectone":
           display8 = "display: none;"
           DatabaseSelection8 = ""
           DatabaseSelection8Records = ""
       elif DatabaseSelection8==None:
           display8 = "display: none;"
           DatabaseSelection8 = ""
           DatabaseSelection8Records = ""
       else:
           display8 = ""
           DatabaseSelection8Average = Medlinedf[DatabaseSelection8].mean(numeric_only=True)
           if pd.isna(DatabaseSelection8Average):
                DatabaseSelection8Records = "No data"
           else:
                DatabaseSelection8Records = DatabaseSelection8Average.round(0).astype(int)

       if DatabaseSelection9=="selectone":
           display9 = "display: none;"
           DatabaseSelection9 = ""
           DatabaseSelection9Records = ""
       elif DatabaseSelection9==None:
           display9 = "display: none;"
           DatabaseSelection9 = ""
           DatabaseSelection9Records = ""
       else:
           display9 = ""
           DatabaseSelection9Average = Medlinedf[DatabaseSelection9].mean(numeric_only=True)
           if pd.isna(DatabaseSelection9Average):
                DatabaseSelection9Records = "No data"
           else:
                DatabaseSelection9Records = DatabaseSelection9Average.round(0).astype(int)
 
       if DatabaseSelection10=="selectone":
           display10 = "display: none;"
           DatabaseSelection10 = ""
           DatabaseSelection10Records = ""
       elif DatabaseSelection10==None:
           display10 = "display: none;"
           DatabaseSelection10 = ""
           DatabaseSelection10Records = ""
       else:
           display10 = ""
           DatabaseSelection10Average = Medlinedf[DatabaseSelection10].mean(numeric_only=True)
           if pd.isna(DatabaseSelection10Average):
                DatabaseSelection10Records = "No data"
           else:
                DatabaseSelection10Records = DatabaseSelection10Average.round(0).astype(int)
       DatabaseList = sorted(DatabaseList)
       DatabaseListString = "; ".join(DatabaseList)
       print(DatabaseListString)

# TopicsUniquedf = df[df['Topics'].str.contains(Topics)]
# TopicsUnique = TopicsUniquedf['UniquePercent'].mean(numeric_only=True)

       TopicMatches = Topicdf.shape[0]

       MedlineMatches = Medlinedf.shape[0]  
        
       UniqueCombined = Topicdf.query('DatabasesUsed.str.contains(@DatabaseListString)')['UniquePercent'].mean(numeric_only=True)
        
       print(UniqueCombined)      
       DataMatch = Topicdf.query('DatabasesUsed.str.contains(@DatabaseListString)')
       DatabaseMatches = DataMatch.shape[0]
        
       if not GreyLiteratureSelection:
           GreyLiteratureAverage = ""
           GreyLitMatches = "0"
           IncludesPercent = Topicdf.query('DatabasesUsed.str.contains(@DatabaseListString)')['DatabaseIncludesPercent'].mean(numeric_only=True)

       else: 
           GreyLiteratureSelection = "; ".join(GreyLiteratureSelection)
           GreyLiteratureAverage = Medlinedf.query('`Other sources searched` == @GreyLiteratureSelection')['Grey Literature'].mean(numeric_only=True)
           GreyLitMatch = Medlinedf.query('`Other sources searched` == @GreyLiteratureSelection')
           GreyLitMatches = GreyLitMatch.shape[0]
           IncludesPercent = Topicdf.query('DatabasesUsed.str.contains(@DatabaseListString)')['GreyLiteratureIncludesPercent'].mean(numeric_only=True)

           if pd.isna(GreyLiteratureAverage):
                GreyLiteratureAverage = "No data"

           else:
                GreyLiteratureAverage = GreyLiteratureAverage.round(0).astype(int)
        
       TotalMedline = int(TotalMedline)  
       TotalScreen = ([TotalMedline, CINAHLAverage, CochraneLibraryAverage, CochraneCentralAverage, ERICAverage, PEDroAverage, PsycINFOAverage, EmbaseAverage, ScopusAverage, WebOfScienceAverage, GreyLiteratureAverage, DatabaseSelection1Records, DatabaseSelection2Records, DatabaseSelection3Records, DatabaseSelection4Records, DatabaseSelection5Records, DatabaseSelection6Records, DatabaseSelection7Records, DatabaseSelection8Records, DatabaseSelection9Records, DatabaseSelection10Records])
       TotalScreen = sum(x if not isinstance(x,str) else 0 for x in TotalScreen)
           
       if TotalScreen==0:
           TotalScreen="No data"
       elif TotalScreen==TotalMedline:
           TotalScreen="No data"
       else:
           TotalScreen = int(float(TotalScreen))

       if TotalScreen=="No data" or pd.isna(TotalScreen) or pd.isna(UniqueCombined) or UniqueCombined==0:
           UniqueAverage = "No data"
       else:
           UniqueAverage = TotalScreen * UniqueCombined
           UniqueAverage = UniqueAverage.round(0).astype(int)

       if TotalScreen=="No data" or pd.isna(TotalScreen) or pd.isna(IncludesPercent):
           IncludesAverage = "No data"
       else:
           IncludesAverage = TotalScreen * IncludesPercent
           IncludesAverage = IncludesAverage.round(0).astype(int)

       if UniqueAverage=="No data" or pd.isna(UniqueAverage):
           AbstractScreenTime = "No data"
       else:
           AbstractScreenAverage = "1.5"
           AbstractScreenAverage = float(AbstractScreenAverage)
           AbstractScreenTime = UniqueAverage * AbstractScreenAverage
           HoursCalc = "60"
           HoursCalc = float(HoursCalc)
           AbstractScreenTime = AbstractScreenTime / HoursCalc
           AbstractScreenTime = round(AbstractScreenTime)
           AbstractScreenTime = str(AbstractScreenTime) + " hrs per reviewer"

       if UniqueAverage=="No data" or pd.isna(UniqueAverage):
           FullTextRecords = "No data"
           FullTextScreenTime = "No data"
           FullTextRetrievalTime = "No data"
           DataExtractionTime = "No data"
       else:
           FullTextRecordsCalc = float("0.035")
           FullTextRecords = UniqueAverage * FullTextRecordsCalc
           FullTextRecords = round(FullTextRecords)
           FullTextScreenCalc = float("4.65")
           FullTextScreenTime = FullTextRecords * FullTextScreenCalc
           HoursCalcFull = float("60")
           FullTextScreenTime = FullTextScreenTime / HoursCalcFull
           FullTextScreenTime = round(FullTextScreenTime)
           FullTextScreenTime = str(FullTextScreenTime) + " hrs per reviewer"
           FullTextRetrievalTime = FullTextRecords * float("4")
           FullTextRetrievalTime = FullTextRetrievalTime / HoursCalcFull
           FullTextRetrievalTime = round(FullTextRetrievalTime)
           FullTextRetrievalTime = str(FullTextRetrievalTime) + " hrs"
           FullTextRecords = str(FullTextRecords)
           DataExtractionCalc = float("53")
           if IncludesAverage=="No data" or pd.isna(IncludesAverage):
                DataExtractionTime = "No data"
           else:
                DataExtractionTime = IncludesAverage * DataExtractionCalc
                DataExtractionTime = DataExtractionTime / HoursCalcFull
                DataExtractionTime = round(DataExtractionTime)
                DataExtractionTime = str(DataExtractionTime) + " hrs per reviewer"
    
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
        AgricultureChecked = ""
        AlliedChecked = ""
        BiochemistryChecked = ""
        BusinessChecked = ""
        DentistryChecked = ""
        DrugsChecked = ""
        EcologyChecked = ""
        EducationChecked = ""
        EngineeringChecked = ""
        EnvironmentalChecked = ""
        ForensicChecked = ""
        HealthInformaticsChecked = ""
        LawEthicsChecked = ""
        LibraryScienceChecked = ""       
        MedicineChecked = ""
        NursingChecked = ""
        PharmacyChecked = ""
        PhysicalChecked = ""
        PoliticalChecked = ""
        PsychologyChecked = ""
        ResearchChecked = ""
        SociologyChecked = ""
        SportsChecked = ""
        ToxicologyChecked = ""
        UrbanChecked = ""
        VeterinaryChecked = ""
        BloodChecked = ""
        CancerChecked = ""
        CardiovascularChecked = ""
        ComplementaryChecked = ""
        CongenitalChecked = ""
        CriticalChecked = ""
        EarChecked = ""
        EmergencyChecked = ""
        EyeChecked = ""
        GeriatricsChecked = ""
        InfectionChecked = ""
        InflammatoryChecked = ""
        InjuriesChecked = ""
        MetabolicChecked = ""
        MusculoskeletalChecked = ""
        NeurologicalChecked = ""
        OccupationalMedChecked = ""
        OralChecked = ""
        PalliativeChecked = ""
        PathologyChecked = ""
        PediatricsChecked = ""
        RenalChecked = ""
        ReproductiveChecked = ""
        RespiratoryTherapyChecked = ""
        SkinChecked = ""
        SleepChecked = ""
        SpaceChecked = ""
        StrokeChecked = ""
        SurgeryChecked = ""
        TelemedicineChecked = ""
        GeneralChecked = ""
        ArtChecked = ""
        AudiologyChecked = ""
        CaregivingChecked = ""
        ChiropracticChecked = ""
        DieteticsChecked = ""
        ImagingChecked = ""
        InfectionPreventionChecked = ""
        MidwiferyChecked = ""
        OccupationalChecked = ""
        PhysiotherapyChecked = ""
        PrehospitalChecked = ""
        ProstheticsChecked = ""
        RecreationChecked = ""
        RespiratoryChecked = ""
        SocialChecked = ""
        SpiritualChecked = ""
        MedicineDisabled = "disabled='disabled'"
        AlliedDisabled = "disabled='disabled'"
        CINAHLChecked = ""
        CochraneLibraryChecked = ""
        CochraneCentralChecked = ""
        EmbaseChecked = ""
        ERICChecked = ""
        PEDroChecked = ""
        PsycINFOChecked = ""
        ScopusChecked = ""
        WebOfScienceChecked = ""
        AlgorithmicChecked = ""
        AuthorSearchChecked = ""
        CitationsChecked = ""
        DiscoveryChecked = ""
        GeneralGreyChecked = ""
        GeneralWebChecked = ""
        GuidelinesChecked = ""
        HandChecked = ""
        HealthTechnologyChecked = ""
        InstitutionalChecked = ""
        NationalChecked = ""
        PersonalCommunicationChecked = ""
        PreprintsChecked = ""
        PointOfCareChecked = ""
        PreviousReviewsChecked = ""
        PriorKnowledgeChecked = ""
        ProtocolsChecked = ""
        ScholarlyChecked = ""
        SubjectSearchedChecked = ""
        ThesesChecked = ""
        TrialRegistriesChecked = ""  
        UpdatesAlertsChecked = ""
        UnknownUnclearChecked = ""
        TopicMatches = ""
        MedlineMatches = ""
        DatabaseMatches = ""
        GreyLitMatches = ""
        AbstractScreenTime = ""
        FullTextRecords = ""
        FullTextRetrievalTime = ""
        FullTextScreenTime = ""
        DataExtractionTime = ""
        
    return render_template("form.html",CINAHLRecords = CINAHLAverage, CochraneLibraryRecords = CochraneLibraryAverage, CochraneCentralRecords = CochraneCentralAverage, ERICRecords = ERICAverage, PEDroRecords = PEDroAverage, PsycINFORecords = PsycINFOAverage, WebOfScienceRecords = WebOfScienceAverage, EmbaseRecords = EmbaseAverage, ScopusRecords = ScopusAverage, IncludesRecords = IncludesAverage, UniqueRecords = UniqueAverage, TotalScreen=TotalScreen, MedlineRecords=TotalMedline, GreyLiteratureRecords=GreyLiteratureAverage, display1 = display1, display2 = display2, display3 = display3, display4 = display4, display5 = display5, display6 = display6, display7 = display7, display8 = display8, display9 = display9, display10 = display10, DatabaseSelection1Name = DatabaseSelection1, DatabaseSelection1Records = DatabaseSelection1Records, DatabaseSelection2Name = DatabaseSelection2, DatabaseSelection2Records = DatabaseSelection2Records, DatabaseSelection3Name = DatabaseSelection3, DatabaseSelection3Records = DatabaseSelection3Records, DatabaseSelection4Name = DatabaseSelection4, DatabaseSelection4Records = DatabaseSelection4Records, DatabaseSelection5Name = DatabaseSelection5, DatabaseSelection5Records = DatabaseSelection5Records, DatabaseSelection6Name = DatabaseSelection6, DatabaseSelection6Records = DatabaseSelection6Records, DatabaseSelection7Name = DatabaseSelection7, DatabaseSelection7Records = DatabaseSelection7Records, DatabaseSelection8Name = DatabaseSelection8, DatabaseSelection8Records = DatabaseSelection8Records, DatabaseSelection9Name = DatabaseSelection9, DatabaseSelection9Records = DatabaseSelection9Records, DatabaseSelection10Name = DatabaseSelection10, DatabaseSelection10Records = DatabaseSelection10Records, MedicineDisplay = MedicineDisplay, AlliedDisplay = AlliedDisplay, AgricultureChecked = AgricultureChecked, AlliedChecked = AlliedChecked, BiochemistryChecked = BiochemistryChecked, BusinessChecked = BusinessChecked, DentistryChecked = DentistryChecked, DrugsChecked = DrugsChecked, EcologyChecked = EcologyChecked, EducationChecked = EducationChecked, EngineeringChecked = EngineeringChecked, EnvironmentalChecked = EnvironmentalChecked, MedicineChecked = MedicineChecked, NursingChecked = NursingChecked, PhysicalChecked = PhysicalChecked, PsychologyChecked = PsychologyChecked, SportsChecked = SportsChecked, VeterinaryChecked = VeterinaryChecked, BloodChecked = BloodChecked, CancerChecked = CancerChecked, CardiovascularChecked = CardiovascularChecked, ComplementaryChecked = ComplementaryChecked, CongenitalChecked = CongenitalChecked, EarChecked = EarChecked, EyeChecked = EyeChecked, GeriatricsChecked = GeriatricsChecked, InfectionChecked = InfectionChecked, InflammatoryChecked = InflammatoryChecked, InjuriesChecked = InjuriesChecked, MetabolicChecked = MetabolicChecked, MusculoskeletalChecked = MusculoskeletalChecked, NeurologicalChecked = NeurologicalChecked, OralChecked = OralChecked, PediatricsChecked = PediatricsChecked, RenalChecked = RenalChecked, ReproductiveChecked = ReproductiveChecked, RespiratoryTherapyChecked = RespiratoryTherapyChecked, SkinChecked = SkinChecked, SleepChecked = SleepChecked, StrokeChecked = StrokeChecked, SurgeryChecked = SurgeryChecked, GeneralChecked = GeneralChecked, ArtChecked = ArtChecked, AudiologyChecked = AudiologyChecked, DieteticsChecked = DieteticsChecked, ImagingChecked = ImagingChecked, OccupationalChecked = OccupationalChecked, PhysiotherapyChecked = PhysiotherapyChecked, PrehospitalChecked = PrehospitalChecked, ProstheticsChecked = ProstheticsChecked, RecreationChecked = RecreationChecked, RespiratoryChecked = RespiratoryChecked, SocialChecked = SocialChecked, SpiritualChecked = SpiritualChecked, AlliedDisabled = AlliedDisabled, MedicineDisabled = MedicineDisabled, CINAHLChecked = CINAHLChecked, CochraneLibraryChecked = CochraneLibraryChecked, CochraneCentralChecked = CochraneCentralChecked, EmbaseChecked = EmbaseChecked, ERICChecked = ERICChecked, PEDroChecked = PEDroChecked, PsycINFOChecked = PsycINFOChecked, ScopusChecked = ScopusChecked, WebOfScienceChecked = WebOfScienceChecked, ThesesChecked = ThesesChecked, CitationsChecked = CitationsChecked, ScholarlyChecked = ScholarlyChecked, HandChecked = HandChecked, GeneralGreyChecked = GeneralGreyChecked, AlgorithmicChecked = AlgorithmicChecked, AuthorSearchChecked = AuthorSearchChecked, DiscoveryChecked = DiscoveryChecked, GeneralWebChecked = GeneralWebChecked, GuidelinesChecked = GuidelinesChecked, HealthTechnologyChecked = HealthTechnologyChecked, InstitutionalChecked = InstitutionalChecked, NationalChecked = NationalChecked, PersonalCommunicationChecked = PersonalCommunicationChecked, PreprintsChecked = PreprintsChecked, PointOfCareChecked = PointOfCareChecked, PreviousReviewsChecked = PreviousReviewsChecked, PriorKnowledgeChecked = PriorKnowledgeChecked, ProtocolsChecked = ProtocolsChecked, SubjectSearchedChecked = SubjectSearchedChecked, TrialRegistriesChecked = TrialRegistriesChecked, UpdatesAlertsChecked = UpdatesAlertsChecked, UnknownUnclearChecked = UnknownUnclearChecked, ForensicChecked = ForensicChecked, HealthInformaticsChecked = HealthInformaticsChecked, LawEthicsChecked = LawEthicsChecked, LibraryScienceChecked = LibraryScienceChecked, PharmacyChecked = PharmacyChecked, PoliticalChecked = PoliticalChecked, ResearchChecked = ResearchChecked, SociologyChecked = SociologyChecked, ToxicologyChecked = ToxicologyChecked, UrbanChecked = UrbanChecked, CriticalChecked = CriticalChecked, EmergencyChecked = EmergencyChecked, OccupationalMedChecked = OccupationalMedChecked, PalliativeChecked = PalliativeChecked, PathologyChecked = PathologyChecked, SpaceChecked = SpaceChecked, TelemedicineChecked = TelemedicineChecked, CaregivingChecked = CaregivingChecked, ChiropracticChecked = ChiropracticChecked, InfectionPreventionChecked = InfectionPreventionChecked, MidwiferyChecked = MidwiferyChecked, TopicMatches = TopicMatches, DatabaseMatches = DatabaseMatches, MedlineMatches = MedlineMatches, GreyLitMatches = GreyLitMatches, AbstractScreenTime = AbstractScreenTime, FullTextRecords = FullTextRecords, FullTextRetrievalTime = FullTextRetrievalTime, FullTextScreenTime = FullTextScreenTime, DataExtractionTime = DataExtractionTime)

if __name__=='__main__':
   app.run()















































































































