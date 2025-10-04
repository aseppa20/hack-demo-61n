INSERT INTO Ajoneuvot (Rekisteri, Merkki, Malli, Valmistusvuosi, Rekisterointi_maa, viime_sijainti, Status) VALUES
('ABC-123', 'Volvo', 'FH16', 2019, 'Viro', 'Suomi', 'aktiivinen'),
('DEF-456', 'Scania', 'R580', 2021, 'Suomi', 'Suomi', 'seisonta'),
('GHI-789', 'Krone', 'CoolLiner', 2018, 'Suomi', 'Viro', 'aktiivinen'),
('JLM-012', 'Volkswagen', 'Passat', 2021, 'Suomi', 'Suomi', 'aktiivinen'),
('AAB-001', 'Volvo', 'V70', 2009, 'Saksa', 'Suomi', 'seisonta'),
('ABD-002', 'Volvo', 'V80', 2001, 'Suomi', 'Suomi', 'seisonta'),
('OPQ-013', 'Volkswagen', 'Golf', 2012, 'Suomi', 'Saksa', 'aktiivinen');

INSERT INTO Tulli (ID, Ylityspaikka, Suunta, Maa, pvm, Tulli_tunnus, Tulli_sijainti, Rekisteri, Maatunnus, Status) VALUES
(C1001, 'Vaalimaa', 'maastalähtö', 'Viro', '2025-10-01 08:42', 'T20251001A', 'Hanko', 'ABC-123', 'FIN' TRUE),
(C1002, 'Tornio', 'maahantulo', 'Ruotsi', '2025-10-03 15:27', 'T20251003B', 'Helsinki Vuosaari', TRUE),
(C1003, 'Nuijamaa', 'maahantulo', 'Venäjä', '2025-09-29 22:13', 'T20250929C', 'Imatra', FALSE);

INSERT INTO Kuljetusyritys (ID, Rekisteri, Kuljettaja, Lahto, Maaranpaa, Kuormantyyppi, Lahtoaika, Saapumisaika, Status) VALUES
(S9001, 'ABC-123', 'J. Niemi', 'Helsinki', 'Tallinna', 'Elintarvikkeet', '2025-10-01 06:30', '2025-10-01 11:00', 'toimitettu'),
(S9002, 'DEF-456', A. Korhonen', 'Oulu', 'Tampere', 'Elektroniikka', '2025-10-03 07:15', '2025-10-03 12:45', 'kesken'),
(S9003, 'GHI-789','K. Nieminen', 'Lappeenranta', 'Pietari', 'Tyhjä perävaunu', '2025-09-29 20:00', '2025-09-29 23:10', 'odottaa');