import random

def generate_star():
    # Types spectraux possibles
    spectral_types = ['O', 'B', 'A', 'F', 'G', 'K', 'M']
    spectral_subtypes = [str(i) for i in range(10)]

    # Génération des caractéristiques
    spectral_type = random.choice(spectral_types) + random.choice(spectral_subtypes)
    if spectral_type[0] == 'O':
        mass = round(random.uniform(16, 50), 2)
        luminosity = round(random.uniform(30_000, 1_000_000), 2)
        temp = round(random.uniform(30_000, 50_000), 2)
        lifespan = round(random.uniform(1, 10), 2)
    elif spectral_type[0] == 'B':
        mass = round(random.uniform(2.1, 16), 2)
        luminosity = round(random.uniform(25, 30_000), 2)
        temp = round(random.uniform(10_000, 30_000), 2)
        lifespan = round(random.uniform(10, 100), 2)
    elif spectral_type[0] == 'A':
        mass = round(random.uniform(1.4, 2.1), 2)
        luminosity = round(random.uniform(5, 25), 2)
        temp = round(random.uniform(7_500, 10_000), 2)
        lifespan = round(random.uniform(100, 1_000), 2)
    elif spectral_type[0] == 'F':
        mass = round(random.uniform(1.04, 1.4), 2)
        luminosity = round(random.uniform(1.5, 5), 2)
        temp = round(random.uniform(6_000, 7_500), 2)
        lifespan = round(random.uniform(1_000, 4_000), 2)
    elif spectral_type[0] == 'G':
        mass = round(random.uniform(0.8, 1.04), 2)
        luminosity = round(random.uniform(0.6, 1.5), 2)
        temp = round(random.uniform(5_000, 6_000), 2)
        lifespan = round(random.uniform(4_000, 10_000), 2)
    elif spectral_type[0] == 'K':
        mass = round(random.uniform(0.45, 0.8), 2)
        luminosity = round(random.uniform(0.08, 0.6), 2)
        temp = round(random.uniform(3_700, 5_000), 2)
        lifespan = round(random.uniform(15_000, 30_000), 2)
    else:  # M
        mass = round(random.uniform(0.08, 0.45), 2)
        luminosity = round(random.uniform(0.0001, 0.08), 2)
        temp = round(random.uniform(2_400, 3_700), 2)
        lifespan = round(random.uniform(50_000, 200_000), 2)

    radius = round(mass ** 0.8, 2)  # Une approximation simple du rayon en fonction de la masse
    metallicity = round(random.uniform(0.1, 3.0), 2)
    rotation_period = round(random.uniform(10, 50), 2)  # En jours
    magnetic_activity = random.choice(['Low', 'Moderate', 'High'])

    star = {
        'Spectral Type': spectral_type,
        'Mass (in Solar masses)': mass,
        'Luminosity (in Solar luminosities)': luminosity,
        'Temperature (K)': temp,
        'Radius (in Solar radii)': radius,
        'Metallicity': metallicity,
        'Rotation Period (days)': rotation_period,
        'Magnetic Activity': magnetic_activity,
        'Lifespan (million years)': lifespan
    }

    return star

# Générer une étoile fictive
star = generate_star()
for key, value in star.items():
    print(f"{key}: {value}")
