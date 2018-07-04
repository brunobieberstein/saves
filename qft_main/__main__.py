import standardize
import evaluate
import parse_input

fname = input('QFT-Datei zum Analysieren: ')

data_in = open(fname, 'r')
data, layout = parse_input.parse_input(data_in)
data_in.close()

conc, status = standardize.transform_to_concs(data, layout)

patientrecords = parse_input.get_patient_records(conc, layout)

print()
for patient, record in sorted(patientrecords.items()):
    test_result = evaluate.evaluate_patient(record)
    if test_result == 1:
        outcome = 'positive'
    elif test_result == 0:
        outcome = 'negative'
    else:
        outcome = 'nicht beurteilbar'
    print ('Ergebnis four Patient', patient ,'ist', outcome + '.')
    
print()
    