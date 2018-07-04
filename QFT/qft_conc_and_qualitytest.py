# -*- coding: utf-8 -*-

import math

import numpy as np

from scipy import stats


STANDARDS = [
    ('S4', 0),
    ('S3', 0.25),
    ('S2', 1),
    ('S1', 4)
    ]
y = np.array([0.25, 1, 4])

    
QUALITY_OK = 0
HIGH_BACKGROUND = 1
LOW_SENSITIVITY = 2
UNRELIABLE_HIGH = 4
UNRELIABLE_LOW = 8
POOR_CORRELATION = 16


TEST_LAYOUT = np.array([
    ['A','B','S1','S1'],
    ['C','D','S2','S2'],
    ['S3','S4','E','F'],
    ['S3','S4','G','H']
    ])
    
TEST_DATA = np.array([
    [0.43, 0.23, 0.5, 0.7],
    [0.21, 0.7, 0.25, 0.25],
    [0.1, 0.002, 0.32, 0.38],
    [0.08, 0.006, 0.05, 0.64]
    ])
    
    
def transform_to_concs(od_data, layout):
    """Transform an array of OD values to an array of concentrations.
    
    Concentrations are calculated from the measured standard values
    contained in the input array.

    In addition, performs a quality check of the standard values.
    
    Returns a tuple of the new concentrations array and a quality indication.
    """

    std_od = get_std_data(od_data, layout)
    std_mean_od = np.mean(std_od, axis=1)
    std_stdev_od = np.std(std_od, axis=1)
    status = QUALITY_OK

    lin = stats.linregress(np.log(std_mean_od)[1:], np.log(y))
    k = lin[0]
    a = math.exp(lin[1])
    conc_data = a*TEST_DATA**k
    
    rvalue = lin[2]
    # Der ELISA liefert gültige Ergebnisse, wenn alle nachstehenden
    # Kriterien erfüllt sind:
    # - Der Mittelwert der OD von Standard 1 muss ≥ 0,600 sein.
    if std_mean_od[3] < 0.6:
        status += LOW_SENSITIVITY
        
    # - Der prozentuale Variationskoeffizient (%CV) der OD-Werte der
    #   Mehrfachbestimmungen von Standard 1 und Standard 2 muss ≤ 15 % sein.
    if np.any(((std_stdev_od/std_mean_od)*100)[2:] >15):
        status += UNRELIABLE_HIGH
        
    # - Die OD-Werte der Mehrfachbestimmungen von Standard 3 und Standard 4
    #   dürfen höchstens um 0,040 OD-Einheiten vom jeweiligen Mittelwert
    #   abweichen.
    if np.any(np.abs(std_mean_od[:2] - (std_od[:2].T)) > 0.04):
        status += UNRELIABLE_LOW
    
    # - Der aus den mittleren Absorptionswerten der Standards berechnete
    #   Korrelationskoeffizient (r) muss ≥ 0,98 sein.
    if rvalue < 0.98:
        status += POOR_CORRELATION
    
    # Werden die obigen Kriterien nicht erfüllt, ist der Test ungültig und
    # muss wiederholt werden.
    # Der Mittelwert der OD des Nullstandards (grüne Verdünnungslösung)
    # sollte ≤ 0,150 sein. Wenn der Mittelwert der OD > 0,150 ist, sollte
    # das Verfahren zum Waschen der Platten überprüft werden.
    if std_mean_od[0] > 0.15:
        status += HIGH_BACKGROUND
    
    
    return conc_data, status


def get_std_data(od_data, layout):
    """Return std OD values from all data sorted by known concentration
    in ascending order."""
    S1_mask = layout == STANDARDS[3][0]
    S2_mask = layout == STANDARDS[2][0]
    S3_mask = layout == STANDARDS[1][0]
    S4_mask = layout == STANDARDS[0][0]
    S1 = od_data[S1_mask]
    S2 = od_data[S2_mask]
    S3 = od_data[S3_mask]
    S4 = od_data[S4_mask]
    return np.vstack([S4, S3, S2, S1])


if __name__ == '__main__':
    conc, status = transform_to_concs(TEST_DATA, TEST_LAYOUT)
    if status != 4:
        print('Expected status==4, got:', status)
    if not np.all(conc > 0):
        print('Problem with calculation detected!')
    print()
    print('Got these concentrations:')
    print(conc)
