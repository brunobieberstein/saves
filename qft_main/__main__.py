import sys
import os

import standardize
import evaluate
import parse_input

fname = sys.argv[1]
if os.path.isdir(fname):
    fname = [os.path.join(fname, f) for f in sorted(os.listdir(fname))]
else:
    fname = [fname]

for f in fname:
    print()
    print('Ergebnisse für Datei', f)
    data_in = open(f, 'r')
    data, layout = parse_input.parse_input(data_in)
    data_in.close()
    
    conc, status = standardize.transform_to_concs(data, layout)
    
    patientrecords = parse_input.get_patient_records(conc, layout)
    
    for patient, record in sorted(patientrecords.items()):
        test_result = evaluate.evaluate_patient(record)
        if '--exclude-negative' in sys.argv:
            if test_result == 0:
                continue
        if test_result == 1:
            outcome = 'positive'
        elif test_result == 0:
            outcome = 'negative'
        else:
            outcome = 'nicht beurteilbar'
        print ('Ergebnis für Patient', patient ,'ist', outcome + '.')
    
print()
    