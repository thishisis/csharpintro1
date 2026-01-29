DROP DATABASE IF EXISTS universe;
CREATE DATABASE universe;
\c universe;

CREATE TABLE galaxy (
    galaxy_id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    galaxy_type TEXT NOT NULL,
    age_in_millions_of_years INT NOT NULL,
    distance_from_earth NUMERIC(10, 2),
    has_black_hole BOOLEAN NOT NULL,
    is_spiral BOOLEAN NOT NULL,
    number_of_stars INT
);

CREATE TABLE star (
    star_id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    galaxy_id INT NOT NULL REFERENCES galaxy(galaxy_id),
    star_type TEXT NOT NULL,
    temperature_kelvin INT NOT NULL,
    mass_solar_units NUMERIC(10, 2),
    is_main_sequence BOOLEAN NOT NULL,
    has_planets BOOLEAN NOT NULL,
    age_in_millions_of_years INT
);

CREATE TABLE planet (
    planet_id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    star_id INT NOT NULL REFERENCES star(star_id),
    planet_type TEXT NOT NULL,
    radius_km INT NOT NULL,
    orbital_period_days NUMERIC(10, 2),
    has_atmosphere BOOLEAN NOT NULL,
    has_life BOOLEAN NOT NULL,
    number_of_moons INT
);

CREATE TABLE moon (
    moon_id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    planet_id INT NOT NULL REFERENCES planet(planet_id),
    moon_type TEXT NOT NULL,
    radius_km INT NOT NULL,
    orbital_period_days NUMERIC(8, 2),
    has_water_ice BOOLEAN NOT NULL,
    is_spherical BOOLEAN NOT NULL,
    surface_temperature_celsius INT
);

INSERT INTO galaxy (name, galaxy_type, age_in_millions_of_years, distance_from_earth, has_black_hole, is_spiral, number_of_stars) VALUES
('Milky Way', 'Spiral', 13600, 0, true, true, 400000000),
('Andromeda', 'Spiral', 10000, 2537000, true, true, 1000000000),
('Triangulum', 'Spiral', 12000, 3000000, false, true, 40000000),
('Messier 87', 'Elliptical', 13240, 53500000, true, false, 1200000000),
('Whirlpool', 'Spiral', 11000, 23000000, true, true, 100000000),
('Sombrero', 'Spiral', 13250, 29000000, true, true, 800000000);

INSERT INTO star (name, galaxy_id, star_type, temperature_kelvin, mass_solar_units, is_main_sequence, has_planets, age_in_millions_of_years) VALUES
('Sun', 1, 'G-type', 5778, 1.0, true, true, 4600),
('Proxima Centauri', 1, 'M-type', 3042, 0.12, true, true, 4850),
('Sirius', 1, 'A-type', 9940, 2.02, true, false, 242),
('Betelgeuse', 1, 'M-type', 3500, 20.0, false, false, 10000),
('Alpha Centauri A', 1, 'G-type', 5790, 1.1, true, true, 6000),
('Vega', 1, 'A-type', 9602, 2.14, true, false, 455),
('Rigel', 1, 'B-type', 12100, 21.0, true, false, 8000),
('Arcturus', 1, 'K-type', 4286, 1.08, false, false, 7100);

INSERT INTO planet (name, star_id, planet_type, radius_km, orbital_period_days, has_atmosphere, has_life, number_of_moons) VALUES
('Mercury', 1, 'Terrestrial', 2439, 88.0, false, false, 0),
('Venus', 1, 'Terrestrial', 6051, 224.7, true, false, 0),
('Earth', 1, 'Terrestrial', 6371, 365.25, true, true, 1),
('Mars', 1, 'Terrestrial', 3389, 687.0, true, false, 2),
('Jupiter', 1, 'Gas Giant', 69911, 4333.0, true, false, 79),
('Saturn', 1, 'Gas Giant', 58232, 10759.0, true, false, 82),
('Uranus', 1, 'Ice Giant', 25362, 30687.0, true, false, 27),
('Neptune', 1, 'Ice Giant', 24622, 60190.0, true, false, 14),
('Proxima b', 2, 'Terrestrial', 7160, 11.2, true, false, 0),
('Proxima c', 2, 'Super-Earth', 8500, 1928.0, false, false, 0),
('Alpha Centauri Bb', 5, 'Terrestrial', 7200, 3.24, false, false, 0),
('Kepler-186f', 1, 'Terrestrial', 7200, 130.0, true, false, 0),
('HD 209458 b', 1, 'Gas Giant', 94400, 3.5, true, false, 0);

INSERT INTO moon (name, planet_id, moon_type, radius_km, orbital_period_days, has_water_ice, is_spherical, surface_temperature_celsius) VALUES
('Moon', 3, 'Rocky', 1737, 27.32, true, true, -23),
('Phobos', 4, 'Rocky', 11, 0.32, false, false, -40),
('Deimos', 4, 'Rocky', 6, 1.26, false, false, -40),
('Io', 5, 'Volcanic', 1821, 1.77, false, true, -143),
('Europa', 5, 'Icy', 1560, 3.55, true, true, -160),
('Ganymede', 5, 'Icy', 2634, 7.15, true, true, -163),
('Callisto', 5, 'Icy', 2410, 16.69, true, true, -139),
('Titan', 6, 'Icy', 2575, 15.95, true, true, -179),
('Rhea', 6, 'Icy', 764, 4.52, true, true, -174),
('Iapetus', 6, 'Icy', 735, 79.33, true, true, -143),
('Dione', 6, 'Icy', 561, 2.74, true, true, -186),
('Tethys', 6, 'Icy', 533, 1.89, true, true, -187),
('Enceladus', 6, 'Icy', 252, 1.37, true, true, -198),
('Mimas', 6, 'Icy', 198, 0.94, true, true, -200),
('Titania', 7, 'Icy', 788, 8.71, true, true, -203),
('Oberon', 7, 'Icy', 761, 13.46, true, true, -198),
('Umbriel', 7, 'Icy', 584, 4.14, true, true, -198),
('Ariel', 7, 'Icy', 578, 2.52, true, true, -213),
('Miranda', 7, 'Icy', 235, 1.41, true, true, -213),
('Triton', 8, 'Icy', 1353, 5.88, true, true, -235),
('Proteus', 8, 'Rocky', 210, 1.12, false, false, -223),
('Nereid', 8, 'Rocky', 170, 360.14, false, false, -223),
('Larissa', 8, 'Rocky', 97, 0.55, false, false, -223);
