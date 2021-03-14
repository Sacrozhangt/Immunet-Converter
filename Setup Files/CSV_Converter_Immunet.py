# -*- coding: utf-8 -*-


#This will be for editing a patient data CSV file into the proper files that Immunet requires.

import pandas as pd
from datetime import date
import csv

def dataframesplitter (InputFrame):
    '''
    Parameters
    ----------
    InputFrame: Pandas Dataframe containing all information required by CDC reporting guidelines

    Returns
    -------
    two formatted Pandas Dataframes containing data entry cells required by MDImmunet
    '''

    #initalizes two arrays with the labels to be moved over

    imm_req = ['Vaccine Group', 'CPT Code', 'Trade Name', 'CVX Code', 'NDC Code',
       'Vaccination Date', 'Administration Route Code', 'Body Site Code',
       'Reaction Code', 'Manufacturer Code', 'Immunization Information Source',
       'Lot Number', 'Provider Name', 'Administered By Name',
       'Sending Organization', 'Financial Class (VFC Eligibility Status)',
       'Vaccine Purchased With (Funding Type)']
    pts_req = ['Patient Status', 'First Name', 'Middle Name', 'Last Name',
       'Name Suffix', 'Birth Date', 'Death Date', 'Mothers First Name',
       'Mothers Maiden Last Name', 'Sex (Gender)', 'Race', 'Ethnicity',
       'Contact Allowed', 'Consent to Share', 'Patient ID',
       'Responsible Party  First Name', 'Responsible Party Middle Name',
       'Responsible Party Last Name', 'Responsible Party Relationship',
       'Street Address', 'PO Box Route Line', 'Other Address Line', 'City',
       'State', 'Zip', 'County', 'Phone', 'Sending Organization']


    new_pts = InputFrame.reindex (columns = pts_req)
    new_imm = InputFrame.reindex (columns = imm_req)


    new_pts_filtered = new_pts.dropna(how = 'all')
    new_imm_filtered = new_imm.dropna(how = 'all')

    return new_pts_filtered, new_imm_filtered

def filenames ():
    '''
    Returns
    -------
    patient file name with the current date
    immunization file name

    '''
    today = date.today()
    datestring = today.strftime("%m%d%Y")
    CL = 'ORGIDNUMBER_CL_' + datestring + '_01.csv'
    IMM = 'ORGIDNUMBER_IMM_' + datestring + '_01.csv'
    return CL, IMM


#read a template CSV that users will enter data into
inFile = pd.read_csv('INPUT_FILE.csv', dtype = "string", index_col='Record Identifier' )

#creates the two separate files and two filenames
PtFile , ImmFile = dataframesplitter(inFile)
CL, IMM = filenames ()

#saves the two files (including quotes) with the filenames
PtFile.to_csv(path_or_buf = CL, quoting=csv.QUOTE_NONNUMERIC)
ImmFile.to_csv(path_or_buf = IMM, quoting=csv.QUOTE_NONNUMERIC)